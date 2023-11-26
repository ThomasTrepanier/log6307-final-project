import random
from itertools import cycle, islice
from time import perf_counter as pc
import numpy as np


def op(choice, x):
    n = len(choice)
    selection = []
    for i in range(x, x + n):
        selection.append(choice[i % n])
    return selection


def nick(choice, x):
    n = len(choice)
    return [choice[i % n] for i in range(x, x + n)]


def fountainhead(choice, x):
    n = len(choice)
    return np.take(choice, range(x, x + n), mode='wrap')


def chepner(choice, x):
    n = len(choice)
    return list(islice(cycle(choice), x, x + n))


results = []
n = 1_000_000
choice = random.sample(range(n), n)
x = random.randint(0, n - 1)

# Correctness
assert op(choice, x) == nick(choice,x) == chepner(choice,x) == list(fountainhead(choice,x))

# Benchmark
for f in op, nick, chepner, fountainhead:
    t0 = pc()
    f(choice, x)
    t1 = pc()
    results.append((t1 - t0, f))

for t, f in sorted(results):
    print(f'{f.__name__}: {t} s')
