from time import time
from ..utils import *

# Function to manage client connections
def handle_client(conn, addr):
    print(f"Connection established with {addr}.")

    while True:
        try:
            data = conn.recv(1024)  # Receive data from the client
            msg_type = get_message_type(data.decode())
            try:
                function_dict[msg_type](conn, addr)
            except Exception as e:
                print(f"{msg_type}: {e}")
        except ConnectionResetError:
            print(f"Client {addr} has disconnected.")
            break
    conn.close()
    print(f"Connection with {addr} closed.")


def handle_ping(conn, addr):
    """Function to handle ping messages."""
    """TODO: kill connection if client is not responding for a certain amount of time."""
    while True:
        try:
            msg = conn.recv(1024).decode()
            
            print(f"Received: {msg}")
            print_address(addr)
            ans = f"pong,{str(time())}"
            conn.sendall(ans.encode())
        except ConnectionResetError:
            print(f"Client {addr} has disconnected.")
            break


def handle_control(conn, addr):
    """Function to handle control messages."""
    pass


def handle_unknown(conn, addr):
    """Function to handle unknown message types."""
    print(f"Received unknown message type from {addr}.")
    conn.sendall("exit".encode())
    conn.close()