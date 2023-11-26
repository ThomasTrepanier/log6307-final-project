linux = platform.system() == "Linux"
windows = platform.system() == "Windows"
macos = platform.system() == "Darwin"

if linux:
    def my_callback(*args, **kwargs):
        print("Doing something @ Linux")
        return

if windows:
    def my_callback(*args, **kwargs):
        print("Doing something @ Windows")
        return
