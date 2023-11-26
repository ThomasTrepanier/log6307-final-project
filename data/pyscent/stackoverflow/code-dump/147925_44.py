def sum_of_even(n):
    if n<=0:
        return 0
    if not n % 2 == 0:
        return sum_of_even(n-1)
    else:
        return n + sum_of_even(n-2)
