import numpy as np
import timeit

# x = np.array("1 2 2 0 0 1 3 5".split(),int)
x = np.random.randint(0, 100, 100000)

def create_index_list(x):
    d = {}
    max_value = -1
    for i,v in enumerate(x):
        if v > max_value:
            max_value = v
        try:
            d[v].append(i)
        except:
            d[v] = [i]
    result_list = []
    for i in range(max_value+1):
        if i in d:
            result_list.append(d[i])
        else:
            result_list.append([])
    return result_list

# print(create_index_list(x))
print(timeit.timeit(stmt='create_index_list(x)', number=1, globals=globals()))

