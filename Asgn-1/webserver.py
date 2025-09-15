# Web Server Lab - CPSC 353 Networks
# Student: [Your Name Here]
# Date: [Date]

# Import socket module
from socket import *
import sys  # In order to terminate the program

# Create a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Fill in start - Bind the socket to server address and server port
# Hint: You need to bind the socket to a specific address and port
# Use serverSocket.bind() method
# Fill in end

# Fill in start - Configure the socket to listen for incoming connections
# Hint: Use serverSocket.listen() method with appropriate backlog
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
        # Fill in start - Receive the HTTP request from the client
        # Hint: Use connectionSocket.recv() to receive data
        # Store the received message in a variable
        # Fill in end
        
        message = # Fill in start - Decode the received message
                 # Hint: Convert bytes to string using .decode()
                 # Fill in end
        
        # Extract the filename from the HTTP request
        filename = message.split()[1]
        
        # Open the requested file
        f = open(filename[1:])  # Remove the leading '/' from filename
        
        outputdata = # Fill in start - Read the content of the file
                    # Hint: Use f.read() to read file content
                    # Fill in end
        
        # Send one HTTP header line into socket
        # Fill in start - Send HTTP response header
        # Hint: Send "HTTP/1.1 200 OK\r\n\r\n" to indicate successful response
        # Use connectionSocket.send() and encode the string
        # Fill in end
        
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        # Close the file
        f.close()
        connectionSocket.close()
        
    except IOError:
        # Send response message for file not found (404 error)
        # Fill in start - Send 404 Not Found response
        # Hint: Send appropriate HTTP 404 response header and message
        # Example: "HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1>404 Not Found</h1></body></html>"
        # Fill in end
        
        # Close client socket
        # Fill in start - Close the connection socket
        # Hint: Use connectionSocket.close()
        # Fill in end

# Close server socket and terminate program
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
