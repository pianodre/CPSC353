# UDP Ping Lab

A simple UDP ping client-server application that simulates packet loss and measures round-trip time.

## Files

- `UDPPingerServer.py` - UDP server that responds to ping messages with 40% packet loss simulation
- `UDPPingerClient.py` - UDP client that sends 10 ping messages and calculates RTT

## How to Run

### 1. Start the Server
```bash
python UDPPingerServer.py
```
The server will start listening on port 12000.

### 2. Run the Client
Open a new terminal and run:
```bash
python UDPPingerClient.py
```

The client will send 10 ping messages and display:
- Response messages from server
- Round-trip time (RTT) for successful pings
- "Request timed out" for lost packets
- Final statistics (packet loss, min/avg/max RTT)

## Expected Output

```
PING localhost:12000

Reply from 127.0.0.1: PING 1 1696008523.123 RTT=0.002s
Request timed out for ping 2
Reply from 127.0.0.1: PING 3 1696008524.456 RTT=0.001s
...

--- localhost ping statistics ---
10 packets transmitted, 6 received, 40.0% packet loss
round-trip min/avg/max = 0.001/0.002/0.003 seconds
```

## Notes

- Server simulates ~40% packet loss
- Client waits 1 second for each response before timing out
- Both programs run on localhost (127.0.0.1) port 12000
