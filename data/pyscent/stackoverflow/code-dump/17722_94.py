from functools import lru_cache

@lru_cache()
def collatz(n):
    sequenceLength = 0
    if n == 1:
        return n
    elif n % 2 == 0:
        return 1 + collatz(n // 2)
    else:  # n % 2 == 1:
        return 1 + collatz(3 * n + 1)
