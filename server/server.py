import socket
import threading

# import server.ping_server as ping_server

# Server IP and Port configuration
HOST = '127.0.0.1'  # Server IP (localhost)
PORT = 65432        # Port for client connections

def handle_ping(conn, addr):
    """Function to handle ping messages."""
    while True:
        try:
            msg = conn.recv(1024).decode()
            print(f"Received ping: {msg}")
            conn.sendall(f"Pong: {msg}, <our_time>".encode())
        except ConnectionResetError:
            print(f"Client {addr} has disconnected.")
            break

# Function to manage client connections
def handle_client(conn, addr):
    print(f"Connection established with {addr}.")

    while True:
        try:
            # data = conn.recv(1024)  # Receive data from the client
            # print(f"Received from {addr}: {data.decode()}")
            # if data.decode().startswith("ping"):
            handle_ping(conn, addr)
            # else:
                # response = f"Server response: {data.decode()}".encode()
            # conn.sendall(response)  # Send the received data back to the client
        except ConnectionResetError:
            print(f"Client {addr} has disconnected.")
            break
    conn.close()
    print(f"Connection with {addr} closed.")

# Start the server
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}...")
        try:        
            while True:
                conn, addr = server_socket.accept()  # Accept a client connection
                thread = threading.Thread(target=handle_client, args=(conn, addr))
                thread.start()  # Start a new thread for each client
                print(f"Active connections: {threading.activeCount() - 1}")
        except KeyboardInterrupt:
            print("\nShutting down server...")

if __name__ == "__main__":
    start_server()