import numpy as np

def f_pp(a,bs):
    i,j = a.shape
    k,l = bs
    esh = i//k,k,j//l,l
    bc = esh[::2]
    sh1,sh2 = np.unravel_index(np.random.permutation(bc[0]*bc[1]),bc)
    ns1,ns2 = np.unravel_index(np.arange(bc[0]*bc[1]),bc)
    out = np.empty_like(a)
    out.reshape(esh)[ns1,:,ns2] = a.reshape(esh)[sh1,:,sh2]
    return out
