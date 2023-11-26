def sublist(x):
    accum = 0
    sub = []
    while accum < len(x):
        if x[accum]== 5:
            return sub
        else:
            sub.append(x[accum])
        accum = accum +1
    return sub

x = [1, 3, 4, 5,6,7,8]
print(sublist(x))
