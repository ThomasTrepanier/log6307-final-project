import numpy as np
import numba as nb

@nb.njit
def mask_more_n(arr, n):
    mask = np.ones(arr.shape, np.bool_)

    current = arr[0]
    count = 0
    for idx, item in enumerate(arr):
        if item == current:
            count += 1
        else:
            current = item
            count = 1
        mask[idx] = count <= n
    return mask
