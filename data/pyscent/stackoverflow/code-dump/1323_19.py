def A_Stefan_row_class(m, n):
    class A0:
        def __getitem__(self, n):
            return n + 1
    class A:
        def __init__(self, a):
            self.a = a
            self.n = 0
            self.value = a[1]
        def __getitem__(self, n):
            while self.n < n:
                self.value = self.a[self.value]
                self.n += 1
            return self.value
    a = A0()
    for _ in range(m):
        a = A(a)
    return a[n]


from collections import defaultdict

def A_Stefan_row_lists(m, n):
    memo = defaultdict(list)
    def a(m, n):
        if not m:
            return n + 1
        if m not in memo:
            memo[m] = [a(m-1, 1)]
        Am = memo[m]
        while len(Am) <= n:
            Am.append(a(m-1, Am[-1]))
        return Am[n]
    return a(m, n)


from itertools import count

def A_Stefan_generators(m, n):
    a = count(1)
    def up(a, x=1):
        for i, ai in enumerate(a):
            if i == x:
                x = ai
                yield x
    for _ in range(m):
        a = up(a)
    return next(up(a, n))


def A_Stefan_paper(m, n):
    next = [0] * (m + 1)
    goal = [1] * m + [-1]
    while True:
        value = next[0] + 1
        transferring = True
        i = 0
        while transferring:
            if next[i] == goal[i]:
                goal[i] = value
            else:
                transferring = False
            next[i] += 1
            i += 1
        if next[m] == n + 1:
            return value


def A_Stefan_generators_2(m, n):
    def a0():
        n = yield
        while True:
            n = yield n + 1
    def up(a):
        next(a)
        a = a.send
        i, x = -1, 1
        n = yield
        while True:
            while i < n:
                x = a(x)
                i += 1
            n = yield x
    a = a0()
    for _ in range(m):
        a = up(a)
    next(a)
    return a.send(n)


def A_Stefan_m_recursion(m, n):
    ix = [None] + [(-1, 1)] * m
    def a(m, n):
        if not m:
            return n + 1
        i, x = ix[m]
        while i < n:
            x = a(m-1, x)
            i += 1
        ix[m] = i, x
        return x
    return a(m, n)


def A_Stefan_function_stack(m, n):
    def a(n):
        return n + 1
    for _ in range(m):
        def a(n, a=a, ix=[-1, 1]):
            i, x = ix
            while i < n:
                x = a(x)
                i += 1
            ix[:] = i, x
            return x
    return a(n)


from itertools import count, islice

def A_Stefan_generator_stack(m, n):
    a = count(1)
    for _ in range(m):
        a = (
            x
            for a, x in [(a, 1)]
            for i, ai in enumerate(a)
            if i == x
            for x in [ai]
        )
    return next(islice(a, n, None))


from itertools import count, islice

def A_Stefan_generator_stack2(m, n):
    a = count(1)
    def up(a):
        i, x = 0, 1
        while True:
            i, x = x+1, next(islice(a, x-i, None))
            yield x
    for _ in range(m):
        a = up(a)
    return next(islice(a, n, None))


def A_Stefan_generator_stack3(m, n):
    def a(m):
        if not m:
            yield from count(1)
        x = 1
        for i, ai in enumerate(a(m-1)):
            if i == x:
                x = ai
                yield x
    return next(islice(a(m), n, None))


def A_Stefan_generator_stack4(m, n):
    def a(m):
        if not m:
            return count(1)
        return (
            x
            for x in [1]
            for i, ai in enumerate(a(m-1))
            if i == x
            for x in [ai]
        )
    return next(islice(a(m), n, None))


def A_templatetypedef(i, n):
    positions = [-1] * (i + 1)
    values = [0] + [1] * i
    
    while positions[i] != n:       
        values[0]    += 1
        positions[0] += 1
            
        j = 1
        while j <= i and positions[j - 1] == values[j]:
            values[j] = values[j - 1]
            positions[j] += 1
            j += 1

    return values[i]

import ctypes
mylib = ctypes.CDLL('./ackermann.so')
mylib.ackermann.argtypes = [ctypes.c_int64, ctypes.c_int64]
mylib.ackermann.restype = ctypes.c_int64

def c_ackermann(m, n):
    return mylib.ackermann(m,n)

funcs = [
    c_ackermann,
    A_Stefan_row_class,
    A_Stefan_row_lists,
    A_Stefan_generators,
    A_Stefan_paper,
    A_Stefan_generators_2,
    A_Stefan_m_recursion,
    A_Stefan_function_stack,
    A_Stefan_generator_stack,
    A_Stefan_generator_stack2,
    A_Stefan_generator_stack3,
    A_Stefan_generator_stack4,
    A_templatetypedef
]

N = 18
args = (
    [(0, n) for n in range(N)] +
    [(1, n) for n in range(N)] +
    [(2, n) for n in range(N)] +
    [(3, n) for n in range(N)]
)

from time import time

def print(*args, print=print, file=open('out.txt', 'w')):
    print(*args)
    print(*args, file=file, flush=True)
    
expect = none = object()
for _ in range(3):
  for f in funcs:
    t = time()
    result = [f(m, n) for m, n in args]
    # print(f'{(time()-t) * 1e3 :5.1f} ms ', f.__name__)
    print(f'{(time()-t) * 1e3 :5.0f} ms ', f.__name__)
    if expect is none:
        expect = result
    elif result != expect:
        raise Exception(f'{f.__name__} failed')
    del result
  print()

  c_ackermann(-1, -1)

