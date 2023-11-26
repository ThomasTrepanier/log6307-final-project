import numpy as np

#pythran export sort_to_bins(int[:],int)

def sort_to_bins(idx, mx):
    if mx==-1: 
        mx = idx.max() + 1
    cnts = np.zeros(mx + 2, int)
    for i in range(idx.size):
        cnts[idx[i] + 2] += 1
    for i in range(3, cnts.size):
        cnts[i] += cnts[i-1]
    res = np.empty_like(idx)
    for i in range(idx.size):
        res[cnts[idx[i]+1]] = i
        cnts[idx[i]+1] += 1
    return [res[cnts[i]:cnts[i+1]] for i in range(mx)]
