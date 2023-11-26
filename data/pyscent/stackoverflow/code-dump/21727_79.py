import numpy as np

#pythran export bincollect(int[:])

def bincollect(a):
    o = [[] for _ in range(a.max()+1)]
    for i,j in enumerate(a):
        o[j].append(i)
    return o
