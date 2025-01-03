import socket

def get_device_name():
    try:
        # Get the device name (hostname)
        device_name = socket.gethostname()
        return device_name
    except Exception as e:
        print(f"Error: {e}")
        return None