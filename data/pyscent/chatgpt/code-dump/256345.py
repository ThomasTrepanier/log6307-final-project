import platform
import os
import winreg

def is_browser_installed(browser_name: str) -> bool:
    system_name = platform.system()

    if system_name == "Windows":
        if browser_name == "chrome":
            try:
                reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_READ) as key:
                    value, _ = winreg.QueryValueEx(key, None)
                    return os.path.exists(value)
            except WindowsError:
                return False

        elif browser_name == "firefox":
            try:
                reg_path = r"SOFTWARE\Mozilla\Mozilla Firefox"
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_READ) as key:
                    value, _ = winreg.QueryValueEx(key, "PathToExe")
                    return os.path.exists(value)
            except WindowsError:
                return False

        else:
            return False

    elif system_name == "Darwin" or system_name == "Linux":
        # ...existing code for macOS and Linux...
        return False

    else:
        return False
