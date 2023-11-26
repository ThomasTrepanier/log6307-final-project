import numpy as np
import numba as nb
import numexpr as ne

@nb.njit(parallel=True)
def func_1(num):
    result = np.empty((num, num),dtype=np.int32)
    for i in nb.prange(result.shape[0]):
        for j in range(result.shape[1]):
            result[i, j] = (i * j) % 10
    return result
