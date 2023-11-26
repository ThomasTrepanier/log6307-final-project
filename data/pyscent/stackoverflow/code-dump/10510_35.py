import numpy as np


def main():
    row_count = 4
    col_count = 5
    a = [[1,2,4],[0,2,3],[1,3,4],[0,2]]

    # iterate through each row, concatenate all indices and convert them to linear

    # numpy append performs copy even if you don't want it, list append is faster
    b = []
    for row_idx, row in enumerate(a):
        b.append(np.array(row, dtype=np.int64) + (row_idx * col_count))

    linear_idxs = np.hstack(b)
    #could skip previous steps if given index inputs well before hand, or in linear index order. 
    c = np.zeros(row_count * col_count)
    c[linear_idxs] = 1
    c = c.reshape(row_count, col_count)
    print(c)


if __name__ == "__main__":
    main()

#output
# [[0. 1. 1. 0. 1.]
#  [1. 0. 1. 1. 0.]
#  [0. 1. 0. 1. 1.]
#  [1. 0. 1. 0. 0.]]
