import timeit
lst = [1, 2, 3, 4, 5, 6, 7, 8]

def python_it():
    global lst
    lst = [*lst[:4], *[x+2 for x in lst[4:]]]

def python_it2():
    global lst
    lst[4:] = [x+2 for x in lst[4:]]


print(timeit.timeit(python_it))
print(timeit.timeit(python_it2))
