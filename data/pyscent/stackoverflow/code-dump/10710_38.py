import itertools as it
import numpy as np

def make_data(n,m):
    I,J = np.where(np.random.random((n,m))<np.random.random((n,1)))
    return [*map(np.ndarray.tolist, np.split(J, I.searchsorted(np.arange(1,n))))]

def pp():
    sz = np.fromiter(map(len,a),int,nrow)
    out = np.zeros((nrow,ncol),int)
    out[np.arange(nrow).repeat(sz),np.fromiter(it.chain.from_iterable(a),int,sz.sum())] = 1
    return out

def ts():
    out = np.zeros((nrow,ncol),int)
    for i, ix in enumerate(a):
        out[i][ix] = 1
    return out

def u9():
    out = np.zeros((nrow,ncol),int)
    for i, (x, y) in enumerate(zip(a, out)):
        y[x] = 1
        out[i] = y
    return out

nrow,ncol = 1000,1000
a = make_data(nrow,ncol)

from timeit import timeit
assert (pp()==ts()).all()
assert (pp()==u9()).all()

print("pp", timeit(pp,number=100)*10, "ms")
print("ts", timeit(ts,number=100)*10, "ms")
print("u9", timeit(u9,number=100)*10, "ms")
