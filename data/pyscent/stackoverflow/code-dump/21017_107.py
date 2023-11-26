import numpy as np
from numpy.lib.stride_tricks import as_strided

def windowstride(a, window):
    return as_strided(a, shape=(a.size - window + 1, window), strides=2*a.strides)

def local_min(a, maxwindow=None, doends=True):
    if doends: a = np.pad(a.astype(float), 1, 'constant', constant_values=np.inf)
    if maxwindow is None: maxwindow = a.size - 1

    mins = []
    for i in range(3, maxwindow + 1):
        for j,w in enumerate(windowstride(a, i)):
            if (w[0] > w[1]) and (w[-2] < w[-1]):
                if (w[1:-1]==w[1]).all():
                    mins.append((j, j + i - 2))

    mins.sort()
    return mins
