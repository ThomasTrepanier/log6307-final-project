import timeit
import numpy as np

lst1 = list(range(0, 10000))
npa = np.array(lst1)
lst2 = list(range(0, 10000))
lst3 = list(range(0, 10000))


def numpy_it():
    global npa
    npa[4:] += 2


def python_it():
    global lst1
    lst1 = [*lst1[:4], *[x+2 for x in lst1[4:]]]


def python_it_slice():
    global lst2
    lst2[4:] = [x+2 for x in lst2[4:]]


def python_inplace():
    global lst3
    for i in range(4, len(lst3)):
        lst3[i] = lst3[i] + 2


n = 10000
print(timeit.timeit(numpy_it, number=n))
print(timeit.timeit(python_it_slice, number=n))
print(timeit.timeit(python_it, number=n))
print(timeit.timeit(python_inplace, number=n))
