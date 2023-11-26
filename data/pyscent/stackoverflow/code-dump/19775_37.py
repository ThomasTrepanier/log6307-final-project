import math

SQRT_5 = math.sqrt(5)

def fibonacci(n):
    return int(((((1 + SQRT_5) / 2) ** n) / SQRT_5) + 0.5 )
