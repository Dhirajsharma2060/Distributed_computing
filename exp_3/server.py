import socket
import threading
# Function to handle communication with each client
def handle_client(client_socket, client_address):
    client_socket.settimeout(300)  # Set timeout to 5 minutes
    print(f"New connection: {client_address}")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break # No more data from the client
            print(f"Message from {client_address}: {message.decode("utf-8")}")
            broadcast(message, client_socket) # Send message to all clients
        except:
            break
    client_socket.close()
    print(f"Connection closed: {client_address}")
# Function to broadcast messages to all connected clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)
# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 5555)) # Bind to all interfaces on port 5555
server_socket.listen(5) # Listen for up to 5 incoming connections
clients = []
print("Server started. Waiting for clients...")
# Accept client connections and handle them in separate threads
while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket, client_address)).start()