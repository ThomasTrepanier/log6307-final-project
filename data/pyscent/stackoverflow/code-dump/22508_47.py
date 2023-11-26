def do(number):
    if number%2 == 1:
        return number -1
    else:
        return number

[do(y) if i%3 == 0 else y for i,y in enumerate(L)]
