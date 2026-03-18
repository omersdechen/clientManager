def print_address(addr):
    """Helper function to print client address."""
    print(f"from {addr[0]}:{addr[1]}")

def get_message_type(message):
    """Helper function to determine the type of message."""
    try:
        msg_type = message.split(',')[0]
    except IndexError:
        msg_type = "unknown"
    return msg_type


