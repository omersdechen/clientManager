from time import time, sleep
from utils import *

def handle_ping(sock):
    """Function to perform pinging the server."""
    while True:
        sleep(1)  # Ping every 5 seconds
        first_time = time()
        message = f"ping"
        sock.sendall(message.encode())
        data = sock.recv(1024)  # Receive the response from the server
        ret_time = time()
        resp = data.decode()
        # print(f"Server response: {resp}")
        data_parts = resp.split(',')
        to_server = (float(data_parts[1]) - first_time) * 1000
        round_time = (float(ret_time - first_time)) * 1000
        print(f"time: {round_time}, to server: {to_server} ms")


def handle_control(conn, addr):
    """Function to handle control messages."""
    pass


def handle_unknown(conn, addr):
    """Function to handle unknown message types."""
    print(f"Received unknown message type from {addr}.")
    # conn.sendall("exit".encode())
    conn.close()