def print_even_between(x, y):
    x = round(x / 2) * 2
    y = round(y / 2) * 2

    for i in range(x, y, 2):
        print(i)  
    print(y)
