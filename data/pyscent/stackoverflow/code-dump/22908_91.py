# https://stackoverflow.com/a/44999009/ @Divakar
def view1D(a): # a is array
    a = np.ascontiguousarray(a)
    void_dt = np.dtype((np.void, a.dtype.itemsize * a.shape[1]))
    return a.view(void_dt).ravel()
