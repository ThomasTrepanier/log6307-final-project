def func(n):
    l = []
    for i in range(n):
        tmp = []
        for j in range(n):
            if j==i:
                tmp.append(0)
            elif j>i:
                tmp.append(9)
            elif j<n:
                tmp.append(5)
        l.append(tmp)
    return l
