import socket
import psutil


def is_app_running(app_name):
    """Check if a specific application is running."""
    for process in psutil.process_iter(['name']):
        if process.info['name'] == app_name:
            return True
    return False


def get_device_name():
    try:
        # Get the device name (hostname)
        device_name = socket.gethostname()
        return device_name
    except Exception as e:
        print(f"Error: {e}")
        return None
