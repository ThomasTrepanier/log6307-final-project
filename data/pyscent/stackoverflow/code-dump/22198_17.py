import timeit
import numpy as np

lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
npa = np.array(lst)


def numpy_it():
    global npa
    npa[4:] += 2


def python_it():
    global lst1
    lst1 = [*lst1[:4], *[x+2 for x in lst1[4:]]]


print(timeit.timeit(numpy_it))
print(timeit.timeit(python_it))
