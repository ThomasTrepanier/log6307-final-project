def fn(n):
    try:
        fn.count += 1
    except AttributeError:
        fn.count = 1

    if n <= 1:
        return n
    elif n > 1 and n % 2 == 0:
        return fn(n/2)
    elif n > 1 and n % 2 > 0:
        return fn(3*n+1)
