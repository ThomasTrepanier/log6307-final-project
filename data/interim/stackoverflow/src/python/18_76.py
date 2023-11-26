def sum_digits(a, b):
    sum = 0
    for i in range(a,b+1):
        for e in (str(i)):
            sum += int(e)
    return sum

print(sum_digits(17, 20))
