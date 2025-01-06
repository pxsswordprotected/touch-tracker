import os
import sys
from pathlib import Path
import winreg as reg

def add_to_startup():
    # Get the path of the Python script
    script_path = os.path.abspath(sys.argv[0])
    
    # Create the key in registry
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    try:
        # Open the key
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE)
        
        # Create the command to run the script
        command = f'pythonw "{script_path}"'
        
        # Set the key
        reg.SetValueEx(key, "FaceTouchTracker", 0, reg.REG_SZ, command)
        
        # Close the key
        reg.CloseKey(key)
        print("Successfully added to startup!")
        
    except Exception as e:
        print(f"Error adding to startup: {str(e)}")

if __name__ == "__main__":
    add_to_startup()