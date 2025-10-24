from socket import *
import sys

# Configuration - Update these with actual email addresses for testing
SENDER_EMAIL = "your_email@gmail.com"  # Replace with your email
RECIPIENT_EMAIL = "recipient@example.com"  # Replace with recipient email
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587

def send_email():
    msg = "\r\n I love computer networks!"
    endmsg = "\r\n.\r\n"
    
    # Choose a mail server (e.g. Google mail server) and call it mailserver
    mailserver = MAIL_SERVER  # Fill in start
    # Fill in end
    
    try:
        # Create socket called clientSocket and establish a TCP connection with mailserver
        # Fill in start
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((mailserver, MAIL_PORT))
        # Fill in end
        
        recv = clientSocket.recv(1024).decode()
        print("Server response:", recv)
        if recv[:3] != '220':
            print('220 reply not received from server.')
            return False
        
        # Send HELO command and print server response.
        heloCommand = 'HELO Alice\r\n'
        clientSocket.send(heloCommand.encode())
        recv1 = clientSocket.recv(1024).decode()
        print("HELO response:", recv1)
        if recv1[:3] != '250':
            print('250 reply not received from server.')
            return False
        
        # Send MAIL FROM command and print server response.
        # Fill in start
        mailFromCommand = f'MAIL FROM: <{SENDER_EMAIL}>\r\n'
        clientSocket.send(mailFromCommand.encode())
        recv2 = clientSocket.recv(1024).decode()
        print("MAIL FROM response:", recv2)
        if recv2[:3] != '250':
            print('250 reply not received from server.')
            return False
        # Fill in end
        
        # Send RCPT TO command and print server response.
        # Fill in start
        rcptToCommand = f'RCPT TO: <{RECIPIENT_EMAIL}>\r\n'
        clientSocket.send(rcptToCommand.encode())
        recv3 = clientSocket.recv(1024).decode()
        print("RCPT TO response:", recv3)
        if recv3[:3] != '250':
            print('250 reply not received from server.')
            return False
        # Fill in end
        
        # Send DATA command and print server response.
        # Fill in start
        dataCommand = 'DATA\r\n'
        clientSocket.send(dataCommand.encode())
        recv4 = clientSocket.recv(1024).decode()
        print("DATA response:", recv4)
        if recv4[:3] != '354':
            print('354 reply not received from server.')
            return False
        # Fill in end
        
        # Send message data.
        # Fill in start
        clientSocket.send(msg.encode())
        # Fill in end
        
        # Message ends with a single period.
        # Fill in start
        clientSocket.send(endmsg.encode())
        recv5 = clientSocket.recv(1024).decode()
        print("Message sent response:", recv5)
        if recv5[:3] != '250':
            print('250 reply not received from server.')
            return False
        # Fill in end
        
        # Send QUIT command and get server response.
        # Fill in start
        quitCommand = 'QUIT\r\n'
        clientSocket.send(quitCommand.encode())
        recv6 = clientSocket.recv(1024).decode()
        print("QUIT response:", recv6)
        clientSocket.close()
        # Fill in end
        
        print("Email sent successfully!")
        return True
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

if __name__ == "__main__":
    print("SMTP Client - Lab 3")
    print("===================")
    print(f"Sender: {SENDER_EMAIL}")
    print(f"Recipient: {RECIPIENT_EMAIL}")
    print(f"Mail Server: {MAIL_SERVER}:{MAIL_PORT}")
    print()
    
    print("Note: Update SENDER_EMAIL and RECIPIENT_EMAIL variables before running.")
    print("For Gmail, you may need to use an App Password instead of your regular password.")
    print()
    
    send_email()
