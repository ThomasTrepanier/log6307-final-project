x = np.array(
        [
            [
                [0 , 1, 1, 0],
                [0 , 2, 3, 0],
                [0 , 4, 5, 0]
            ],
            [
                [0 , 6, 7, 0],
                [0 , 7, 8, 0],
                [0 , 9, 5, 0]
            ]
        ])

xx = np.array(
        [
            [
                [0 , 0, 0, 0],
                [0 , 2, 3, 0],
                [0 , 0, 0, 0]
            ],
            [
                [0 , 0, 0, 0],
                [0 , 7, 8, 0],
                [0 , 0, 0, 0]
            ]
        ])

def check_edges(x):

    idx = x.shape
    chunk = np.prod(idx[:-2])
    x = x.reshape((chunk*idx[-2], idx[-1]))
    for block in range(chunk):
        z = x[block*idx[-2]:(block+1)*idx[-2], :]
        if not np.all(z[:, 0] == 0):
            return False
        if not np.all(z[:, -1] == 0):
            return False
        if not np.all(z[0, :] == 0):
            return False
        if not np.all(z[-1, :] == 0):
            return False

    return True
