def print_rows(n, limit):
    if n < limit:
        numbers = range(1, n + 1) if n % 2 == 1 else reversed(range(1, n + 1))
        print(''.join(map(str, numbers)))
        print_rows(n + 1, limit)


def print_pyramid_recursive(n):
    if n > 0:
        print_rows(1, n)


print_pyramid_recursive(10)
