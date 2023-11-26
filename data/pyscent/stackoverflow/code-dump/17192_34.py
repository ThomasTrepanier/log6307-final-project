def fn(n):
    try:
        fn.count += 1
    except AttributeError:
        fn.count = 1

    if n <= 1:
        return n
    return fn((3*n + 1) if n % 2 else (n / 2))
