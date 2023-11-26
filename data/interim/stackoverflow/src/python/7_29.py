import numpy as np
from scipy.signal import argrelmax
from itertools import groupby


def local_max_scipy(a):
    start = 0
    result = [[a[0] - 1, 0, 0]]  # this is to guarantee the left edge is included
    for k, g in groupby(a):
        length = sum(1 for _ in g)
        result.append([k, start, length])
        start += length
    result.append([a[-1] - 1, 0, 0])  # this is to guarantee the right edge is included

    arr = np.array(result)
    maxima, = argrelmax(arr[:, 0])
    return arr[maxima]


test03 = np.array([2, 2, 10, 4, 4, 4, 5, 6, 7, 2, 6, 5, 5, 7, 7, 1, 1])
output = local_max_scipy(test03)

for val, start, length in output:
    print(f'set of {length} maxima start:{start} end:{start + length}')
