import random

orderliness = 0.75

def tuplify(x, y):
    return (orderliness * y + random.gauss(0,1), x)

values = [i+1 for i in range(20)]
print(values)
pairs = list(map(tuplify, values, range(len(values))))
pairs.sort()
partially_ordered_values = [p[1] for p in pairs]
print(partially_ordered_values)
