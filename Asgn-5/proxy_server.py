#!/usr/bin/env python3
"""
HTTP Web Proxy Server with Caching
CPSC 353 - Networks - Lab 5

This proxy server:
1. Accepts HTTP GET requests from clients
2. Forwards requests to web servers
3. Caches responses for improved performance
4. Handles various content types (HTML, images, etc.)
"""

from socket import *
import sys
import os
import hashlib

# Create cache directory if it doesn't exist
if not os.path.exists("./cache"):
    os.makedirs("./cache")

def get_cache_filename(url):
    """Generate a cache filename from URL using hash"""
    return "./cache/" + hashlib.md5(url.encode()).hexdigest() + ".cached"

def parse_request(request):
    """Parse HTTP request to extract method, URL, and host"""
    try:
        lines = request.split('\r\n')
        # Parse request line: GET http://www.example.com/path HTTP/1.1
        request_line = lines[0].split()
        method = request_line[0]
        url = request_line[1]
        
        # Extract host and path from URL
        if url.startswith('http://'):
            url = url[7:]  # Remove 'http://'
        elif url.startswith('https://'):
            url = url[8:]  # Remove 'https://'
        
        # Split host and path
        if '/' in url:
            host, path = url.split('/', 1)
            path = '/' + path
        else:
            host = url
            path = '/'
        
        # Remove port from host if present
        if ':' in host:
            host = host.split(':')[0]
        
        return method, host, path, url
    except Exception as e:
        print(f"Error parsing request: {e}")
        return None, None, None, None

def main():
    # Check command line arguments
    if len(sys.argv) <= 1:
        print('Usage: python proxy_server.py <port>')
        print('Example: python proxy_server.py 8888')
        sys.exit(2)
    
    # Create a server socket, bind it to a port and start listening
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    
    # Fill in start - Prepare server socket
    port = int(sys.argv[1])
    tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcpSerSock.bind(('', port))
    tcpSerSock.listen(5)
    # Fill in end
    
    print(f'Proxy server ready on port {port}...')
    print(f'Access via: http://localhost:{port}/www.example.com')
    print('Press Ctrl+C to stop the server\n')
    
    while True:
        # Start receiving data from the client
        print('Ready to serve...')
        
        # Fill in start - Accept connection from client
        tcpCliSock, addr = tcpSerSock.accept()
        print(f'Received a connection from: {addr}')
        # Fill in end
        
        try:
            # Fill in start - Receive request from client
            message = tcpCliSock.recv(4096).decode()
            
            if not message:
                tcpCliSock.close()
                continue
            
            print(f'Request:\n{message[:200]}...\n')
            # Fill in end
            
            # Parse the request
            method, host, path, url = parse_request(message)
            
            if not method or method != 'GET':
                print('Only GET method is supported')
                error_response = 'HTTP/1.1 400 Bad Request\r\n\r\n'
                tcpCliSock.send(error_response.encode())
                tcpCliSock.close()
                continue
            
            # Generate cache filename
            cache_file = get_cache_filename(url)
            
            # Check if the object is in cache
            try:
                # Fill in start - Try to open cached file
                with open(cache_file, 'rb') as f:
                    print(f'Cache HIT for {url}')
                    print(f'Reading from cache: {cache_file}\n')
                    
                    # Read cached response and send to client
                    cached_data = f.read()
                    tcpCliSock.send(cached_data)
                    print('Sent cached response to client\n')
                # Fill in end
                
            except IOError:
                # Fill in start - Cache MISS: fetch from web server
                print(f'Cache MISS for {url}')
                print(f'Fetching from web server: {host}{path}\n')
                
                # Create a socket to connect to the web server
                c = socket(AF_INET, SOCK_STREAM)
                
                try:
                    # Fill in start - Connect to web server
                    hostn = host
                    port = 80
                    c.connect((hostn, port))
                    # Fill in end
                    
                    # Fill in start - Create and send HTTP request to web server
                    # Reconstruct HTTP request
                    request_to_server = f"GET {path} HTTP/1.1\r\n"
                    request_to_server += f"Host: {host}\r\n"
                    request_to_server += "Connection: close\r\n"
                    request_to_server += "\r\n"
                    
                    c.send(request_to_server.encode())
                    # Fill in end
                    
                    # Fill in start - Receive response from web server
                    response = b''
                    while True:
                        data = c.recv(4096)
                        if not data:
                            break
                        response += data
                    
                    print(f'Received {len(response)} bytes from web server\n')
                    # Fill in end
                    
                    # Fill in start - Cache the response
                    with open(cache_file, 'wb') as cache:
                        cache.write(response)
                        print(f'Cached response to: {cache_file}\n')
                    # Fill in end
                    
                    # Fill in start - Send response to client
                    tcpCliSock.send(response)
                    print('Sent response to client\n')
                    # Fill in end
                    
                except Exception as e:
                    print(f'Error connecting to web server: {e}')
                    error_response = 'HTTP/1.1 502 Bad Gateway\r\n\r\n'
                    error_response += f'Error: Could not connect to {host}\r\n'
                    tcpCliSock.send(error_response.encode())
                
                finally:
                    c.close()
                # Fill in end
        
        except Exception as e:
            print(f'Error handling request: {e}\n')
        
        finally:
            # Fill in start - Close client socket
            tcpCliSock.close()
            # Fill in end
    
    tcpSerSock.close()

if __name__ == "__main__":
    main()
