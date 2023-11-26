def max_num(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3

print(max_num(-10, 0, 10)) # returns 10
print(max_num(-10, 5, -30)) # returns 5
print(max_num(-5, -10, -10)) # returns -5
