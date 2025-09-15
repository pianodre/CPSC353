# Web Server Lab - CPSC 353 Networks

## Assignment Overview
This lab teaches the basics of socket programming for TCP connections in Python. You will develop a web server that handles one HTTP request at a time.

## Objectives
- Learn socket programming fundamentals
- Understand HTTP request/response format
- Implement file serving functionality
- Handle error cases (404 Not Found)

## Files in this Template
- `webserver.py` - Main server code (skeleton to complete)
- `HelloWorld.html` - Sample HTML file for testing
- `README.md` - This instruction file

## Your Task
Complete the skeleton code in `webserver.py` by filling in the sections marked with:
```python
# Fill in start
# Fill in end
```

### Required Implementations

1. **Socket Binding** - Bind the server socket to an address and port
2. **Socket Listening** - Configure the socket to listen for connections
3. **Receive HTTP Request** - Receive and decode client requests
4. **File Reading** - Read requested file content
5. **HTTP Response Header** - Send proper HTTP response headers
6. **404 Error Handling** - Handle file not found errors

## Running the Server

1. Complete the code in `webserver.py`
2. Place HTML files in the same directory as the server
3. Run the server:
   ```bash
   python3 webserver.py
   ```
4. Test from a browser or another machine:
   ```
   http://[SERVER_IP]:[PORT]/HelloWorld.html
   ```

## Testing Instructions

### Successful Request Test
1. Start your server
2. Navigate to `http://localhost:[PORT]/HelloWorld.html`
3. You should see the Hello World page

### 404 Error Test
1. Try accessing a non-existent file: `http://localhost:[PORT]/nonexistent.html`
2. You should receive a "404 Not Found" message

## Implementation Hints

### Socket Binding
```python
serverSocket.bind(('localhost', 6789))  # or use ('', 6789) for all interfaces
```

### Socket Listening
```python
serverSocket.listen(1)  # Allow 1 pending connection
```

### Receiving Data
```python
message = connectionSocket.recv(1024).decode()
```

### HTTP Response Headers
- Success: `"HTTP/1.1 200 OK\r\n\r\n"`
- Not Found: `"HTTP/1.1 404 Not Found\r\n\r\n"`

### 404 Response Example
```python
response = "HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1>404 Not Found</h1></body></html>"
connectionSocket.send(response.encode())
```

## Common Issues and Solutions

### Port Already in Use
- Change the port number in your code
- Or wait a few minutes for the port to be released

### Permission Denied
- Use ports above 1024 (e.g., 6789, 8080)
- Don't use reserved ports (80, 443, etc.)

### File Not Found During Development
- Ensure HTML files are in the same directory as `webserver.py`
- Check file permissions
- Verify filename spelling and case

## Submission Requirements

Submit the following:
1. **Complete `webserver.py`** with all fill-in sections completed
2. **Screenshots** showing:
   - Successful file serving (HelloWorld.html displayed in browser)
   - 404 error handling (error message displayed)
   - Terminal output showing server status

## Grading Criteria
- [ ] Server binds to socket correctly
- [ ] Server listens for connections
- [ ] HTTP requests are received and parsed
- [ ] Files are served with proper HTTP headers
- [ ] 404 errors are handled appropriately
- [ ] Code is clean and well-commented
- [ ] Screenshots demonstrate functionality

## Additional Notes
- The server handles one request at a time (single-threaded)
- Remember to close sockets properly
- Test thoroughly before submission
- Document any assumptions or design decisions

## Getting Help
- Review socket programming documentation
- Check HTTP protocol specifications
- Test incrementally as you implement each section
- Use print statements for debugging
# CPSC353
