def digit(n):
    even = 0
    odd = 0
    string = str(n)
    for i in string:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
    return even - odd
n = 282
print(digit(n)) #12
