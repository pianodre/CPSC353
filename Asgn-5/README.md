# Lab 5: HTTP Web Proxy Server with Caching

## Overview
This is a simple HTTP web proxy server that handles GET requests and caches responses for improved performance. The proxy acts as an intermediary between clients and web servers.

## Features
- ✅ Handles HTTP GET requests
- ✅ Forwards requests to web servers
- ✅ Caches responses to disk
- ✅ Serves cached content on subsequent requests
- ✅ Supports all content types (HTML, images, CSS, JS, etc.)
- ✅ Proper error handling

## Files
- `proxy_server.py` - Main proxy server implementation
- `test_client.py` - Simple client for testing the proxy
- `README.md` - This file
- `cache/` - Directory for cached responses (created automatically)

## How It Works

```
Client → Proxy Server → Web Server
       ←              ←
```

1. Client sends HTTP GET request to proxy
2. Proxy checks if response is cached
   - **Cache HIT**: Returns cached response immediately
   - **Cache MISS**: Forwards request to web server, caches response, returns to client
3. Subsequent requests for the same URL are served from cache

## Running the Proxy Server

### Start the Server
```bash
python3 proxy_server.py <port>
```

Example:
```bash
python3 proxy_server.py 8888
```

The server will start listening on the specified port (e.g., 8888).

## Testing the Proxy

### Method 1: Using the Test Client
```bash
python3 test_client.py <proxy_port> <target_url>
```

Example:
```bash
python3 test_client.py 8888 www.example.com
```

### Method 2: Using a Web Browser

#### Direct URL Method
In your browser's address bar, type:
```
http://localhost:8888/www.example.com
http://localhost:8888/www.google.com
http://localhost:8888/info.cern.ch
```

#### Configure Browser to Use Proxy
You can configure your browser to use the proxy for all requests:

**Firefox:**
1. Go to Settings → Network Settings
2. Select "Manual proxy configuration"
3. HTTP Proxy: `localhost`
4. Port: `8888`
5. Check "Use this proxy server for all protocols"
6. Click OK

**Chrome/Edge:**
1. Go to Settings → System → Open proxy settings
2. Configure proxy settings for your OS
3. Set HTTP proxy to `localhost:8888`

**Safari:**
1. Go to Preferences → Advanced → Proxies
2. Check "Web Proxy (HTTP)"
3. Server: `localhost`, Port: `8888`

Then simply visit any HTTP website (e.g., `http://www.example.com`)

### Method 3: Using curl
```bash
curl -x http://localhost:8888 http://www.example.com
```

### Method 4: Using wget
```bash
wget -e use_proxy=yes -e http_proxy=localhost:8888 http://www.example.com
```

## Testing Cache Functionality

1. First request (Cache MISS):
   ```bash
   python3 test_client.py 8888 www.example.com
   ```
   Server output: `Cache MISS for www.example.com`

2. Second request (Cache HIT):
   ```bash
   python3 test_client.py 8888 www.example.com
   ```
   Server output: `Cache HIT for www.example.com`

The second request should be noticeably faster!

## Viewing Cached Files

Cached responses are stored in the `cache/` directory with MD5-hashed filenames:
```bash
ls -lh cache/
```

To view a cached file:
```bash
cat cache/<filename>.cached
```

## Example Output

### Server Side:
```
Proxy server ready on port 8888...
Access via: http://localhost:8888/www.example.com
Press Ctrl+C to stop the server

Ready to serve...
Received a connection from: ('127.0.0.1', 54321)
Request:
GET http://www.example.com HTTP/1.1
Host: www.example.com
...

Cache MISS for www.example.com
Fetching from web server: www.example.com/

Received 1256 bytes from web server
Cached response to: ./cache/abc123def456.cached
Sent response to client
```

### Client Side:
```
Connecting to proxy server at localhost:8888...
Connected!

Sending request:
GET http://www.example.com HTTP/1.1
Host: www.example.com
Connection: close

Receiving response...
============================================================
RESPONSE RECEIVED:
============================================================
Headers:
HTTP/1.1 200 OK
Content-Type: text/html
...

Body (first 500 chars):
<!doctype html>
<html>
<head>
    <title>Example Domain</title>
...
```

## Supported Websites

The proxy works with any HTTP website. Some examples:
- `http://www.example.com` - Simple test page
- `http://info.cern.ch` - First website ever created
- `http://www.columbia.edu` - University website
- `http://neverssl.com` - Specifically for testing HTTP

**Note:** HTTPS websites require additional SSL/TLS handling not implemented in this basic proxy.

## Implementation Details

### Key Components:

1. **Socket Server** - Listens for client connections on specified port
2. **Request Parser** - Extracts method, host, and path from HTTP requests
3. **Cache Manager** - Uses MD5 hashing to generate unique cache filenames
4. **HTTP Client** - Forwards requests to web servers
5. **Response Handler** - Sends responses back to clients

### Cache Strategy:
- Cache key: MD5 hash of the full URL
- Cache location: `./cache/` directory
- Cache format: Raw HTTP response (headers + body)
- No expiration: Cached files persist until manually deleted

## Clearing the Cache

To clear all cached responses:
```bash
rm -rf cache/*
```

## Troubleshooting

### Port already in use
```
Error: [Errno 48] Address already in use
```
Solution: Use a different port or kill the process using that port:
```bash
lsof -ti:8888 | xargs kill -9
```

### Connection refused
- Ensure the proxy server is running
- Check that you're using the correct port number
- Verify firewall settings

### 502 Bad Gateway
- The target web server may be down
- Check your internet connection
- Some servers block proxy requests

## Assignment Submission

Include:
1. ✅ Complete `proxy_server.py` code
2. ✅ Screenshots showing:
   - Proxy server running
   - Browser accessing website through proxy
   - Server console showing cache HIT and MISS
   - Cached files in the cache directory
3. ✅ This README with testing instructions

## Code Structure

The proxy server includes all required "Fill in start/end" sections:
- Server socket setup and binding
- Client connection acceptance
- Request receiving and parsing
- Cache file reading
- Web server connection
- HTTP request forwarding
- Response receiving and caching
- Response sending to client
- Socket cleanup

## Notes

- This is a simple educational proxy supporting only HTTP GET requests
- HTTPS is not supported (requires SSL/TLS)
- No authentication or access control
- No cache expiration policy
- Single-threaded (handles one request at a time)

## Author
CPSC 353 - Computer Networks
Lab 5 Assignment
