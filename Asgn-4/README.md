# ICMP Ping Lab

A raw-socket ICMP echo application that measures round-trip time (RTT).  
This script pings several **target hosts on different continents** (Princeton, UFRJ, ETH Zurich, Auckland) and prints per-ping results plus a summary.

## Files

- `ICMPPinger.py` – sends ICMP Echo Requests and prints replies/timeouts and summary stats

## How to Run

### 1. Change host to proper link in ping("host", count=4, timeout=1.0) 

### 2. Run the Script (macOS)

sudo python3 ICMPPinger.py 

## Expected Output

PING www.google.com (142.250.188.228) with Python ICMP:
Reply from 142.250.188.228: bytes=8 icmp_seq=1 ttl=115 time=10.495 ms
Reply from 142.250.188.228: bytes=8 icmp_seq=2 ttl=115 time=9.557 ms
Reply from 142.250.188.228: bytes=8 icmp_seq=3 ttl=115 time=9.070 ms
Reply from 142.250.188.228: bytes=8 icmp_seq=4 ttl=115 time=6.536 ms

--- www.google.com ping statistics ---
4 packets transmitted, 4 received, 0.0% packet loss
rtt min/avg/max = 6.536/8.915/10.495 ms









