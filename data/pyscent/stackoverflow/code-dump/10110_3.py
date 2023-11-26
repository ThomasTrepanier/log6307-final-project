def f_recursive1(n):
    if n <= 1:
        return 0
    elif n % 2 == 0:
        return n - 1 + f_recursive1(n-2)
    else:  # n odd
        return n - 2 + f_recursive1(n-2)
