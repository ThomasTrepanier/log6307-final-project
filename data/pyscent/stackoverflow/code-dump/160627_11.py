from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n, p):
    "Calculate Fibonacci(n) modulo p"
    if n < 3:
        return [0, 1, 1][n]
    if n % 2 == 0:
        m = n // 2
        v1 = fibonacci(m - 1, p)
        v2 = fibonacci(m, p)
        return (2*v1 + v2) * v2 % p
    else:
        m = (n + 1) // 2
        v1 = fibonacci(m, p) ** 2
        v2 = fibonacci(m - 1, p) ** 2
        return (v1 + v2) % p


print(fibonacci(500, 997))
#=> 836
print(fibonacci(1000, 997))
#=> 996
