# Web Server Lab - CPSC 353 Networks

## 👥 Group Members
- **Dylan Ernst**
- **Torki Alghamdi**
- **Arya Kumar**
- **Michael Serpa**

---

## 📋 Assignment Overview
This lab teaches the basics of socket programming for TCP connections in Python. You will develop a web server that handles one HTTP request at a time, serving HTML files and handling HTTP requests/responses.

## 🎯 Learning Objectives
- Learn socket programming fundamentals in Python
- Understand HTTP request/response format and headers
- Implement file serving functionality with proper content types
- Handle error cases (404 Not Found) gracefully
- Practice network programming concepts

## 📁 Project Files
- `webserver.py` - Main server implementation (completed)
- `HelloWorld.html` - Sample HTML file for testing server functionality
- `styles.css` - External stylesheet for HelloWorld.html (following web development best practices)
- `README.md` - This comprehensive documentation file

## ✨ Features Implemented
- ✅ TCP socket binding and listening
- ✅ HTTP request parsing and handling
- ✅ File serving with proper HTTP headers
- ✅ Content-Type and Content-Length headers
- ✅ 404 error handling with custom error page
- ✅ Support for HTML and CSS files
- ✅ Clean connection handling and resource cleanup

## 🚀 Prerequisites
- Python 3.x installed on your system
- Basic understanding of HTTP protocol
- Network programming concepts
- Terminal/Command line access

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

## 🏃‍♂️ How to Run the Server

### Quick Start
1. **Navigate to the project directory:**
   ```bash
   cd /path/to/your/project/directory
   ```

2. **Start the web server:**
   ```bash
   python3 webserver.py
   ```

3. **You should see:**
   ```
   Ready to serve...
   ```

4. **Open your web browser and visit:**
   - Main page: `http://localhost:6789/` or `http://localhost:6789/HelloWorld.html`
   - Test 404: `http://localhost:6789/nonexistent.html`

### Alternative Testing Methods
- **From another machine on the same network:**
  ```
  http://[YOUR_IP_ADDRESS]:6789/HelloWorld.html
  ```
- **Using curl command:**
  ```bash
  curl http://localhost:6789/HelloWorld.html
  ```

## 🧪 Testing Instructions

### ✅ Successful Request Test
1. **Start your server** (you should see "Ready to serve..." message)
2. **Open browser** and navigate to `http://localhost:6789/HelloWorld.html`
3. **Expected result:** Beautiful Hello World page with styling loads successfully
4. **Check terminal:** Server should show connection activity

### ❌ 404 Error Test
1. **Try accessing a non-existent file:** `http://localhost:6789/nonexistent.html`
2. **Expected result:** "404 Not Found" error page displays
3. **Verify:** Error is handled gracefully without server crash

### 🔄 Multiple Request Test
1. **Refresh the page multiple times**
2. **Try different valid/invalid URLs**
3. **Expected result:** Server continues to respond to each request

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

## 🛠️ Troubleshooting

### 🚫 Port Already in Use Error
```
OSError: [Errno 48] Address already in use
```
**Solutions:**
- Wait 2-3 minutes for the port to be released
- Change port number in `webserver.py` (line 15): `serverSocket.bind(('', 8080))`
- Kill existing processes: `lsof -ti:6789 | xargs kill -9`

### 🔒 Permission Denied
```
OSError: [Errno 13] Permission denied
```
**Solutions:**
- Use ports above 1024 (current: 6789 ✅)
- Don't use reserved ports (80, 443, 22, etc.)
- Run with appropriate user permissions

### 📁 File Not Found During Development
```
FileNotFoundError: [Errno 2] No such file or directory
```
**Solutions:**
- Ensure all files are in the same directory as `webserver.py`
- Check file permissions: `ls -la *.html *.css`
- Verify filename spelling and case sensitivity
- Make sure `HelloWorld.html` and `styles.css` exist

### 🌐 Browser Connection Issues
**Solutions:**
- Check firewall settings
- Try `127.0.0.1:6789` instead of `localhost:6789`
- Clear browser cache
- Try a different browser or incognito mode

### 🐛 Server Stops Responding
**Solutions:**
- Check terminal for error messages
- Restart the server (Ctrl+C, then `python3 webserver.py`)
- Verify no infinite loops in your code

## 📋 Submission Requirements

Submit the following files:
1. **`webserver.py`** - Complete implementation with all sections filled
2. **`HelloWorld.html`** - Test HTML file (provided)
3. **`styles.css`** - Stylesheet for HTML (provided)
4. **Screenshots** demonstrating:
   - ✅ Successful file serving (HelloWorld.html displayed in browser)
   - ❌ 404 error handling (error message displayed)
   - 🖥️ Terminal output showing server status and requests

## 📊 Grading Criteria
- [ ] **Socket Programming (25%)** - Server binds and listens correctly
- [ ] **HTTP Handling (25%)** - Requests are received and parsed properly
- [ ] **File Serving (25%)** - Files served with correct HTTP headers
- [ ] **Error Handling (15%)** - 404 errors handled appropriately
- [ ] **Code Quality (10%)** - Clean, well-commented, and organized code

## 📝 Additional Notes
- **Architecture:** Single-threaded server (handles one request at a time)
- **Protocol:** HTTP/1.1 with proper headers and connection management
- **Security:** Basic implementation - not production-ready
- **Performance:** Suitable for educational purposes and local testing

## 🆘 Getting Help
- **Documentation:** Review Python socket programming docs
- **Protocol:** Check HTTP/1.1 specification (RFC 2616)
- **Debugging:** Use print statements to trace request/response flow
- **Testing:** Test incrementally as you implement each section
- **Office Hours:** Contact instructor or TA for additional support

## 🎯 Learning Outcomes
Upon completion, you will understand:
- TCP socket programming fundamentals
- HTTP protocol structure and headers
- Client-server communication patterns
- Error handling in network applications
- File I/O operations in web servers

---

**Course:** CPSC 353 - Computer Networks  
**Institution:** [Your University]  
**Semester:** Fall 2025
