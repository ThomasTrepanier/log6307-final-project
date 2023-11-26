import numpy as np
import numba as nb
from simple_benchmark import BenchmarkBuilder, MultiArgument

b = BenchmarkBuilder()

bins = np.array([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5])

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

@b.add_function(warmups=True)
def MSeifert(arr, n):
    return mask_more_n(arr, n)

from scipy.ndimage.morphology import binary_dilation

@b.add_function()
def Divakar_1(a, N):
    k = np.ones(N,dtype=bool)
    m = np.r_[True,a[:-1]!=a[1:]]
    return a[binary_dilation(m,k,origin=-(N//2))]

@b.add_function()
def Divakar_2(a, N):
    k = np.ones(N,dtype=bool)
    return a[binary_dilation(np.ediff1d(a,to_begin=a[0])!=0,k,origin=-(N//2))]

@b.add_function()
def Divakar_3(a, N):
    m = np.r_[True,a[:-1]!=a[1:],True]
    idx = np.flatnonzero(m)
    c = np.diff(idx)
    return np.repeat(a[idx[:-1]],np.minimum(c,N))

from skimage.util import view_as_windows

@b.add_function()
def Divakar_4(a, N):
    m = np.r_[True,a[:-1]!=a[1:]]
    w = view_as_windows(m,N)
    idx = np.flatnonzero(m)
    v = idx<len(w)
    w[idx[v]] = 1
    if v.all()==0:
        m[idx[v.argmin()]:] = 1
    return a[m]

@b.add_function()
def Divakar_5(a, N):
    m = np.r_[True,a[:-1]!=a[1:]]
    w = view_as_windows(m,N)
    last_idx = len(a)-m[::-1].argmax()-1
    w[m[:-N+1]] = 1
    m[last_idx:last_idx+N] = 1
    return a[m]

@b.add_function()
def PaulPanzer(a,N):
    mask = np.empty(a.size,bool)
    mask[:N] = True
    np.not_equal(a[N:],a[:-N],out=mask[N:])
    return mask

import random

@b.add_arguments('array size')
def argument_provider():
    for exp in range(2, 20):
        size = 2**exp
        yield size, MultiArgument([np.array([random.randint(0, 5) for _ in range(size)]), 3])

r = b.run()
import matplotlib.pyplot as plt

plt.figure(figsize=[10, 8])
r.plot()
