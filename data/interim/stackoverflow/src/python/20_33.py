def summer_69(arr):
    pop = []
    for i in arr:
        if i <=9 and i>=6:
            continue
        else:
            pop.append(i)
    return pop
