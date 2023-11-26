from numba import njit

@njit
def f(u):
    out = np.zeros(len(u), np.int64)
    a = out[0] = u[0]
    for i in range(1, len(u)):
        if u[i] == 1:
            if u[i - 1] == 0:
                a += 1
            out[i] = a
    return out

f(df.servo_in_position.to_numpy())

array([0, 0, 1, 0, 2, 2, 0, 0, 3, 0, 4, 0, 5, 5, 5, 0, 0, 0, 6, 6, 0, 0, 0])
