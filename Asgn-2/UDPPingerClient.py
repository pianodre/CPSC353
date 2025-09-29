import socket
import time

# Server configuration
SERVER_HOST = 'localhost'  # or '127.0.0.1'
SERVER_PORT = 12001
TIMEOUT = 1.0  # 1 second timeout
NUM_PINGS = 10

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(TIMEOUT)

print(f"PING {SERVER_HOST}:{SERVER_PORT}")
print()

# Statistics tracking
packets_sent = 0
packets_received = 0
min_rtt = float('inf')
max_rtt = 0
total_rtt = 0

for sequence_number in range(1, NUM_PINGS + 1):
    # Create ping message with format: "Ping sequence_number time"
    send_time = time.time()
    message = f"Ping {sequence_number} {send_time}"
    
    try:
        # Send ping message
        packets_sent += 1
        client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))
        
        # Wait for response
        response, server_address = client_socket.recvfrom(1024)
        receive_time = time.time()
        
        # Calculate RTT
        rtt = receive_time - send_time
        packets_received += 1
        
        # Update statistics
        total_rtt += rtt
        min_rtt = min(min_rtt, rtt)
        max_rtt = max(max_rtt, rtt)
        
        # Print response
        print(f"Reply from {server_address[0]}: {response.decode().strip()} RTT={rtt:.3f}s")
        
    except socket.timeout:
        print(f"Request timed out for ping {sequence_number}")
    except Exception as e:
        print(f"Error sending ping {sequence_number}: {e}")

# Close socket
client_socket.close()

# Print statistics
print()
print(f"--- {SERVER_HOST} ping statistics ---")
print(f"{packets_sent} packets transmitted, {packets_received} received, {((packets_sent - packets_received) / packets_sent * 100):.1f}% packet loss")

if packets_received > 0:
    avg_rtt = total_rtt / packets_received
    print(f"round-trip min/avg/max = {min_rtt:.3f}/{avg_rtt:.3f}/{max_rtt:.3f} seconds")
