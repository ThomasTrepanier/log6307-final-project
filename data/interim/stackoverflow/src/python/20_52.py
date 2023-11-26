def _which_python(self):
    """Decides which python executable we'll embed in the launcher script."""
    allowed_executables = ["python", "python3"]
    if WINDOWS:
        allowed_executables += ["py.exe -3", "py.exe -2"]
...
