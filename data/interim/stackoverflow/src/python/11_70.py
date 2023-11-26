import timeit

A = np.arange(0, 20, 1)
# print(A)
x = 3


def fun():
    return [x < i < 7 for i in A]


def fun2():
    return (A < 7) & (A > 3)


def fun3():
    return np.logical_and(x < A, A < 7)

def fun4():
    return [i < 7 and i > x for i in A]


print('fun()', timeit.timeit('fun()', number=10000, globals=globals()))
print('fun2()', timeit.timeit('fun2()', number=10000, globals=globals()))
print('fun3()', timeit.timeit('fun3()', number=10000, globals=globals()))
print('fun4()', timeit.timeit('fun4()', number=10000, globals=globals()))
