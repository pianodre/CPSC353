# SMTP Lab - Assignment 3

This project implements a simple SMTP client that sends email using raw socket programming without using Python's `smtplib` module.

## Files

- `smtp_client.py` - Basic implementation following the skeleton template exactly
- `smtp_client_enhanced.py` - Enhanced version with better error handling and configuration
- `README.md` - This documentation file

## SMTP Protocol Implementation

The client implements the following SMTP commands in sequence:

1. **Connection**: Establish TCP connection to mail server
2. **HELO**: Identify the client to the server
3. **MAIL FROM**: Specify the sender's email address
4. **RCPT TO**: Specify the recipient's email address
5. **DATA**: Indicate start of message content
6. **Message**: Send the actual email content
7. **End Message**: Send "." to indicate end of message
8. **QUIT**: Close the connection

## Code Structure

### Fill-in Sections Completed:

1. **Mail Server Configuration**:
   ```python
   mailserver = "smtp.gmail.com"
   ```

2. **Socket Connection**:
   ```python
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((mailserver, mailport))
   ```

3. **MAIL FROM Command**:
   ```python
   mailFromCommand = 'MAIL FROM: <your_email@example.com>\r\n'
   clientSocket.send(mailFromCommand.encode())
   recv2 = clientSocket.recv(1024).decode()
   ```

4. **RCPT TO Command**:
   ```python
   rcptToCommand = 'RCPT TO: <recipient@example.com>\r\n'
   clientSocket.send(rcptToCommand.encode())
   recv3 = clientSocket.recv(1024).decode()
   ```

5. **DATA Command**:
   ```python
   dataCommand = 'DATA\r\n'
   clientSocket.send(dataCommand.encode())
   recv4 = clientSocket.recv(1024).decode()
   ```

6. **Message Sending**:
   ```python
   clientSocket.send(msg.encode())
   ```

7. **End Message**:
   ```python
   clientSocket.send(endmsg.encode())
   recv5 = clientSocket.recv(1024).decode()
   ```

8. **QUIT Command**:
   ```python
   quitCommand = 'QUIT\r\n'
   clientSocket.send(quitCommand.encode())
   recv6 = clientSocket.recv(1024).decode()
   clientSocket.close()
   ```

## Usage Instructions

### Basic Version (`smtp_client.py`):
1. Update the email addresses in the MAIL FROM and RCPT TO commands
2. Run: `python smtp_client.py`

### Enhanced Version (`smtp_client_enhanced.py`):
1. Update the configuration variables at the top:
   ```python
   SENDER_EMAIL = "your_email@gmail.com"
   RECIPIENT_EMAIL = "recipient@example.com"
   ```
2. Run: `python smtp_client_enhanced.py`

## Important Notes

### Mail Server Considerations:
- **Gmail**: Uses port 587 for STARTTLS, but this basic implementation connects to port 587 without encryption
- **Authentication**: Modern mail servers require authentication (username/password or app passwords)
- **Security**: This implementation doesn't include STARTTLS or authentication

### Testing Recommendations:
1. Try different mail servers (Gmail, Yahoo, university mail server)
2. Test from different network locations (home vs campus)
3. Check spam/junk folders for received emails
4. Some servers may reject connections from residential IP addresses

### Potential Issues:
- **Port blocking**: ISPs may block port 25 (SMTP)
- **Authentication required**: Most modern servers require authentication
- **Encryption required**: Many servers require STARTTLS
- **Spam filtering**: Emails may be classified as spam

## SMTP Response Codes

- `220`: Service ready
- `250`: Requested mail action okay, completed
- `354`: Start mail input (after DATA command)
- `221`: Service closing transmission channel (after QUIT)

## Assignment Completion

✅ **Complete code**: All fill-in sections have been implemented  
✅ **SMTP protocol**: Proper sequence of SMTP commands  
✅ **Socket programming**: Raw socket implementation without smtplib  
✅ **Error handling**: Response code checking for each command  

The code is ready for submission and testing. Remember to update email addresses and check spam folders when testing.
