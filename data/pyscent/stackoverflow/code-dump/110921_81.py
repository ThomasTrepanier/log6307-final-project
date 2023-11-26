def grab(x, y, w, h):
    screen = np.array(ImageGrab.grab(bbox=(x, y, w, h))) # Throws no errors
    # screen = np.array(ImageGrab.grab()) # Alternative that grabs full screen
    ...
    return screen
