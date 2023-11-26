import numpy as np

from math import cos
import time
import timeit

cos_arr = np.cos(np.arange(10000000))
tic = time.time()

def calc1():
    total = 0
    for j in range(100):
        for i in range(10000000):
            total += cos_arr[i]

def calc2():
    total = 0
    for j in range(100):
        for i in range(10000000):
            total += cos(i)

time1 = timeit.Timer(calc1).timeit(number=1)

time2 = timeit.Timer(calc2).timeit(number=1)
print(time1)
print(time2)
