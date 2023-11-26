from timeit import repeat
import sys

sys.setrecursionlimit(999999)

setup = '''
from functools import cache

def A(m, n):
    if not m:
        return n + 1
    return A(m - 1, A(m, n - 1)) if n else A(m - 1, 1)

@cache
def B(m, n):
    if not m:
        return n + 1
    return B(m - 1, B(m, n - 1)) if n else B(m - 1, 1)

m, n = 3, 8
'''

codes = [
    'A(m, n)',
    'Ackermann = cache(A); Ackermann(m, n)',
    'B.cache_clear(); B(m, n)',
]

for code in codes:
    t = min(repeat(code, setup, number=1))
    print(f'{t*1e3:6.2f} ms ', code)
