def sum_digits(a, b):
    sum = 0
    for i in range(a, b + 1):
        number = i
        while (number > 0):
            sum += number % 10
            number = number // 10
    return sum

print(sum_digits(17, 20))
