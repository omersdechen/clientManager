from handlers import handle_ping, handle_control

# Server IP and Port configuration
HOST = '127.0.0.1'  # Server IP (localhost)
PORT = 65432        # Port for client connections

function_dict = {
    "ping": handle_ping,
    "control": handle_control
}