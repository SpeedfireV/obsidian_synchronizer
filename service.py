# TODO: Make service working
import sys

import time
import subprocess
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket

from sys_info import is_app_running

# Configuration
target_app_name = "Obsidian.exe"  # Replace with the target app's executable name
check_interval = 15  # Seconds between checks for the app
script_execution_interval = 2  # Seconds between script execution

def run_script():
    print("Script is running...")
    subprocess.run([sys.executable, "git_functions.py"])

class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "TestService"
    _svc_display_name_ = "Test Service"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        self.main()

    def main(self):
        while True:
            if is_app_running(target_app_name):
                print(f"{target_app_name} is running. Executing script...")
                while is_app_running(target_app_name):
                    run_script()
                    time.sleep(script_execution_interval)
            else:
                print(f"{target_app_name} is not running. Waiting...")
            time.sleep(check_interval)

if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(AppServerSvc)