def beginning(x):
    n = 0
    lst = []
    while "bye" not in x[n] and n < 10:
        lst.append(x[n])
        n = n + 1
    return lst
