from numba import njit

@njit
def unique_cols_nb(a):
    n_cols = a.shape[1]
    out = np.zeros(n_cols, dtype=np.int32)
    for i in range(n_cols):
        init = a[0, i]
        for j in a[1:, i]:
            if j != init:
                break
        else:
            out[i] = 1
    return out
