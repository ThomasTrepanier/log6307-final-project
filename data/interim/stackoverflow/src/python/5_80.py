def beginning(x):
    ls = []
    idx = 0
    while idx<10:
        if x[idx]=="bye":
            break
        ls.append(x[idx])
        idx+=1
    return ls
