import numpy as np
import numba as nb
import numexpr as ne

def method2(X,Y,cx,cy,r):
    """Numexpr method"""
    res = ne.evaluate('((X-cx)**2 + (Y-cy)**2) < r**2')
    return res

@nb.njit(fastmath=True,parallel=True)
def method3(X,Y,cx,cy,r):
    acc=0
    for i in nb.prange(X.shape[0]):
        if ((X[i]-cx)**2 + (Y[i]-cy)**2) < r**2:
            acc+=1
    return acc
