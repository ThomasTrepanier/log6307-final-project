def beginning(lis):
    ls = []
    counter = 1
    for st in lis:
        if (st != "bye") and (counter <=10):
            ls.append(st)
        else:
            return ls
        counter += 1
