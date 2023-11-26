def _win_os_check():
    """
    Quick Sanity check for Windows OS: look for fmod bug issue 16744.
    """
    try:
        a = arange(13 * 13, dtype= float64).reshape(13, 13)
        a = a % 17  # calls fmod
        linalg.eig(a)
    except Exception:
        msg = ("The current Numpy installation ({!r}) fails to "
                "pass a sanity check due to a bug in the windows runtime. "
                "See this issue for more information: "
                "https://developercommunity.visualstudio.com/content/problem/1207405/fmod-after-an-update-to-windows-2004-is-causing-a.html")
        raise RuntimeError(msg.format(__file__)) from None

if sys.platform == "win32" and sys.maxsize > 2**32:
    _win_os_check()

del _win_os_check
