from fractions import Fraction
import math
from functools import reduce

def naive(n):
    return sum(x**2 * sum(range(x+1)) for x in range(n+1))

def lcm(ints):
    return reduce(lambda r, i: r * i // math.gcd(r, i), ints)

def polynomial(xys):
    xs, ys = zip(*xys)
    n = len(xs)
    A = [[Fraction(x**i) for i in range(n)] for x in xs]
    b = list(ys)
    for _ in range(2):
        for i0 in range(n):
            for i in range(i0 + 1, n):
                f = A[i][i0] / A[i0][i0]
                for j in range(i0, n):
                    A[i][j] -= f * A[i0][j]
                b[i] -= f * b[i0]
        A = [row[::-1] for row in A[::-1]]
        b.reverse()
    coeffs = [b[i] / A[i][i] for i in range(n)]
    denominator = lcm(c.denominator for c in coeffs)
    coeffs = [int(c * denominator) for c in coeffs]
    horner = str(coeffs[-1])
    for c in coeffs[-2::-1]:
        horner += ' * n'
        if c:
            horner = f"({horner} {'+' if c > 0 else '-'} {abs(c)})"
    return f'{horner} // {denominator}'

print(polynomial((x, naive(x)) for x in range(6)))
