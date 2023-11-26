import numpy as np

def unit(elem):
    if elem < 0:
        elem = 0
    else:
        elem = 1
a = np.array([[1, 2, -0.5], [0.5, 2, 3]])
vfunc = np.vectorize(unit)
vfunc(a)

# array([[1, 1, 0], [1, 1, 1]])
