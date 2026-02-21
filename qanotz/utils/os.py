"""
Source code file for my basic notes app using Tkinter.
This file checks the operating system and provides utility functions related to the OS.
"""

import platform
import os
from pathlib import Path

def get_os():
    return platform.system()

def get_appdata_dir() -> str:
    if get_os() == "Windows":
        return str(os.getenv('APPDATA'))
    elif get_os() == "Darwin":
        return os.path.expanduser('~/Library/Application Support')
    else:
        return os.path.expanduser('~/.config')
    
def ensure_dir(path) -> bool:
    path_obj = Path(path)
    if path_obj.exists() and path_obj.is_dir():
        return True
    else:
        os.makedirs(path, exist_ok=True)
        return True
    
if __name__ == "__main__":
    print(f"Operating System: {get_os()}")
    print(f"AppData Directory: {get_appdata_dir()}")
    print(f"Does AppData Directory Exist? {ensure_dir(f"{get_appdata_dir()}/notes_app")}")
    