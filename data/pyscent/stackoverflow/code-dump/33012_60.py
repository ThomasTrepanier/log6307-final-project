def sublist(x):
    count = 0
    new = []
    if 5 in x:
        while(x[count] != 5):
            new.append(x[count])
            count += 1
        return new
        
    else:
        return x
