# cordinates: np.ndarray(n, 2)
def find_nearest(cordinates, x, y):
    x_d = np.abs(cordinate[:, 0] - x)
    y_d = np.abs(cordinate[:, 1] - y)
    nearest_idx = np.argmin(x_d  + y_d)
    return cordinate[nearest_idx]
