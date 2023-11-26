import numpy as np

def diamond(n):
    a, b = np.eye(n, dtype=int), np.eye(n, dtype=int)[:,::-1]

    c, d = np.hstack((b,a[:,1:])), np.hstack((a,b[:,1:]))

    return np.vstack((c, d[1:,:]))
