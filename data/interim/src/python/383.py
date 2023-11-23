def is_browser_installed(browser_name: str) -> bool:
    # ...existing code...
    if system_name == "Windows":
        # Specify the full path to the chrome.exe and firefox.exe executables
        chrome_path = r"C:\Path\to\chrome.exe"
        firefox_path = r"C:\Path\to\firefox.exe"
        if browser_name == "chrome":
            return os.path.exists(chrome_path)
        elif browser_name == "firefox":
            return os.path.exists(firefox_path)
        else:
            return False
    # ...remaining code...
