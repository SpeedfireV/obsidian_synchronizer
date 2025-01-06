import os
import subprocess
import sys
import time

from dotenv import load_dotenv

from sys_info import is_app_running

# Configuration
target_app_name = "Obsidian.exe"  # Replace with the target app's executable name
check_interval = 15  # Seconds between checks for the app
script_execution_interval = 2  # Seconds between script executions

def run_script():
    print("Script is running...")
    subprocess.run([sys.executable, os.getcwd() + "\git_functions.py"])

if __name__ == '__main__':
    while True:
        if is_app_running(target_app_name):
            print(f"{target_app_name} is running. Executing script...")
            while is_app_running(target_app_name):
                run_script()
                time.sleep(script_execution_interval)
        else:
            print(f"{target_app_name} is not running. Waiting...")
        time.sleep(check_interval)