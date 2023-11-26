def sum_digits(a, b):
    total = 0
    for number in range(a,b+1):
        total += sum(int(digit) for digit in str(number))
    return total
