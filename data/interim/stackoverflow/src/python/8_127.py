from math import cos
import time
import numpy as np
from numba import jit



def calc(n):
    x = 1
    y = 1
    z = 1
    total = cos(x) + cos(y) + cos(z)
    for x in range(n, int((n/3 - 1)),-1): #I only want to pick X from n-2 to  n/3 -1 , after that we will repeat.
        cosx = cos(x)
        for y in range(max(int(((n-x)/2))-1,1),min(int(n-x),int(n/3))): #I would only pick number that will not be choosen for the z
                z = n-x-y #Infer the z, taking the rest in account
                temp = cosx + cos(y) + cos(z)
                if temp > total: total = temp
    return total

tic = time.clock()
total = calc(10000)
print(time.clock()-tic)

print (total)
