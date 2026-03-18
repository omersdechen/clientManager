from time import sleep, time
import socket

# import client.ping_client as ping_client


# Start the client
def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))  # Connect to the server
        while True:
            data = client_socket.recv(1024).decode()
            msg_type = get_message_type(data)

            # ping_server(client_socket)
            # message = input("Enter your message (type 'exit' to quit): ")
            # if message.lower() == 'exit':
            #     print("Closing the connection...")
            #     break
            # client_socket.sendall(message.encode())  # Send the message to the server
            #   # Receive the response from the server
            # print(f"Server response: {data.decode()}")
    print("Connection terminated.")

if __name__ == "__main__":
    start_client()