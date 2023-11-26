def fibo(n: int) -> int:
    if n <= 1:
        fibo = 1
    else:
        fibo = fibo(n - 1) + fibo(n - 2)
    return fibo
