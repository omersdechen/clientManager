import socket
# Client IP and Port configuration
HOST = '127.0.0.1'  # Server's IP address (localhost)
PORT = 65432        # Port the server is listening on
# Start the client
def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))  # Connect to the server
        
        while True:
            message = input("Enter your message (type 'exit' to quit): ")
            if message.lower() == 'exit':
                print("Closing the connection...")
                break
            client_socket.sendall(message.encode())  # Send the message to the server
            data = client_socket.recv(1024)  # Receive the response from the server
            print(f"Server response: {data.decode()}")
    
    print("Connection terminated.")
if __name__ == "__main__":
    start_client()