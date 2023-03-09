import socket
import threading

# Define constants for the client
HOST = 'localhost'
PORT = 8000

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Function to handle incoming messages


def receive_messages():
    while True:
        try:
            # Receive data from the server
            data = client_socket.recv(1024)
            if not data:
                break

            # Print the message to the console
            print(data.decode())
        except:
            client_socket.close()
            break


# Create a new thread to handle incoming messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    # Get input from the user
    message = input()

    # Send the message to the server
    client_socket.send(message.encode())
