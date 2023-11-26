def is_hardlink(path):
    try:
        os.readlink(path)
        return True
    except:
        return False
