# icmp_ping.py
from socket import *
import os, sys, struct, time, select

ICMP_ECHO_REQUEST = 8  

def checksum(source: bytes) -> int:
    """
    RFC 1071 checksum over the supplied bytes (works in Py3).
    """
    if len(source) % 2:
        source += b'\x00'
    s = 0
    for i in range(0, len(source), 2):
        s += (source[i] << 8) + source[i + 1]
        s = (s & 0xffff) + (s >> 16)
    return ~s & 0xffff

def receiveOnePing(mySocket, ID, timeout, destAddr):
    timeLeft = timeout
    while True:
        start = time.time()
        r, _, _ = select.select([mySocket], [], [], timeLeft)
        if not r:
            return "Request timed out."

        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(2048)

        # IP header
        ver_ihl = recPacket[0]
        ihl = (ver_ihl & 0x0F) * 4        
        ttl = recPacket[8]                   

        
        icmp_offset = ihl
        icmp_type, icmp_code, icmp_chk, pkt_id, seq = struct.unpack(
            '!BBHHH', recPacket[icmp_offset:icmp_offset+8]
        )

        if icmp_type == 0 and pkt_id == ID:   # Echo Reply for our ID
            
            ts_bytes = recPacket[icmp_offset+8:icmp_offset+16]
            if len(ts_bytes) == 8:
                timeSent = struct.unpack('!d', ts_bytes)[0]
                rtt_ms = (timeReceived - timeSent) * 1000.0
                data_len = len(recPacket) - (icmp_offset + 8)
                return f"Reply from {destAddr}: bytes={data_len} icmp_seq={seq} ttl={ttl} time={rtt_ms:.3f} ms"

        timeLeft -= (time.time() - start)
        if timeLeft <= 0:
            return "Request timed out."

def sendOnePing(mySocket, destAddr, ID, seq=1):
    
    header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, 0, ID, seq)
    data = struct.pack('!d', time.time())

    chksum = checksum(header + data)          # <-- no htons()
    header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, chksum, ID, seq)

    packet = header + data
    mySocket.sendto(packet, (destAddr, 1))

    mySocket.sendto(packet, (destAddr, 1))

def doOnePing(destAddr, timeout, seq):
    icmp_proto = getprotobyname("icmp")
    mySocket = socket(AF_INET, SOCK_RAW, icmp_proto)
    mySocket.setsockopt(SOL_SOCKET, SO_RCVBUF, 65536)

    myID = os.getpid() & 0xFFFF
    sendOnePing(mySocket, destAddr, myID, seq)
    reply = receiveOnePing(mySocket, myID, timeout, destAddr)
    mySocket.close()
    return reply

# User API 
def ping(host, count=4, timeout=1.0):
    """
    Send ICMP echo requests to 'host'. Prints per-packet replies and a summary.
    """
    dest = gethostbyname(host)
    print(f"PING {host} ({dest}) with Python ICMP:")
    sent = 0
    received = 0
    rtts = []

    for seq in range(1, (count if count else 1_000_000) + 1):
        sent += 1
        line = doOnePing(dest, timeout, seq)
        print(line)

        if line.startswith("Reply from"):
            received += 1
            # Extract RTT in ms if present
            try:
                rtt_ms = float(line.split("time=")[1].split()[0])
                rtts.append(rtt_ms)
            except Exception:
                pass

        if count and seq >= count:
            break
        time.sleep(1)

    # Summary 
    loss = 100.0 * (sent - received) / max(1, sent)
    if rtts:
        mn, mx, avg = min(rtts), max(rtts), sum(rtts) / len(rtts)
        print(f"\n--- {host} ping statistics ---")
        print(f"{sent} packets transmitted, {received} received, {loss:.1f}% packet loss")
        print(f"rtt min/avg/max = {mn:.3f}/{avg:.3f}/{mx:.3f} ms")
    else:
        print(f"\n--- {host} ping statistics ---")
        print(f"{sent} packets transmitted, {received} received, {loss:.1f}% packet loss")

if __name__ == "__main__":
    ping("www.auckland.ac.nz", count=4, timeout=1.0) 