def sum_of_even(n):
    sum1 = 0
    if n == 0:
        return sum1

    elif n % 2 == 0:
        sum1 += n
    
    return sum1 + sum_of_even(n - 1)

