from handlers import handle_ping, handle_control

# Client IP and Port configuration
HOST = '127.0.0.1'  # Server's IP address (localhost)
PORT = 65432        # Port the server is listening on

function_dict = {
    "ping": handle_ping,
    "control": handle_control
}