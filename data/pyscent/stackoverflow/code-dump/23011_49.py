import numba

@numba.njit
def fwd_numba(a,b,c):
    for i in range(N):
        c[a[i]]=b[i]

@numba.njit
def inv_numba(a,b,c):
    for i in range(N):
        c[i]=b[a[i]]
