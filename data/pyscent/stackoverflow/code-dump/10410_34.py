import numpy as np
from scipy.sparse import csr_matrix
from itertools import accumulate


def ragged2csr(inds):
    offset = len(inds[0])
    lens = [len(x) for x in inds]
    indptr = list(accumulate(lens))
    indptr = np.array([x - offset for x in indptr])
    indices = np.array([val for sublist in inds for val in sublist])
    n = indices.size
    data = np.ones(n)
    return csr_matrix((data, indices, indptr))

