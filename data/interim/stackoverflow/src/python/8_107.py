def find_qt():
    import os

    path = os.environ['PATH']

    dll_dir = os.path.dirname(__file__) + '\\Qt\\bin'
    if os.path.isfile(dll_dir + '\\Qt5Core.dll'):
        path = dll_dir + ';' + path
        os.environ['PATH'] = path
    else:
        for dll_dir in path.split(';'):
            if os.path.isfile(dll_dir + '\\Qt5Core.dll'):
                break
        else:
            raise ImportError("unable to find Qt5Core.dll on PATH")

    try:
        os.add_dll_directory(dll_dir)
    except AttributeError:
        pass


find_qt()
del find_qt
