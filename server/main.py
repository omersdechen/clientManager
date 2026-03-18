import socket
import threading

from config import *
from utils import *
from handlers import *

def get_message_type(msg):
    """Function to parse incoming messages."""
    msg_type = msg.split(',')[0]
    return msg_type

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
        except KeyboardInterrupt:
            print("\nShutting down server...")

if __name__ == "__main__":
    start_server()