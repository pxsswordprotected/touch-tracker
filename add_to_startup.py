import os
import sys
from pathlib import Path
import winreg as reg

def add_to_startup():
    # get path of the Python script
    script_path = os.path.abspath(sys.argv[0])
    
    # create  key in registry
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    try:
        # open  key
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE)
        
        command = f'pythonw "{script_path}"'
        
        reg.SetValueEx(key, "FaceTouchTracker", 0, reg.REG_SZ, command)
        
        reg.CloseKey(key)
        print("Successfully added to startup!")
        
    except Exception as e:
        print(f"Error adding to startup: {str(e)}")

if __name__ == "__main__":
    add_to_startup()