import socket
import threading
# Function to receive messages from the server
def receive_messages(client_socket):
    client_socket.settimeout(300)  # Set timeout to 5 minutes
    while True:
        try:
            message = client_socket.recv(1024)
            print(f"\nNew message: {message.decode("utf-8")}")
        except:
            print("Connection lost.")
            break
# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5555)) # Connect to the server
# Start the thread for receiving messages
threading.Thread(target=receive_messages, args=(client_socket,)).start()
# Send messages to the server
while True:
    message = input()
    if message:
        client_socket.send(message.encode("utf-8"))