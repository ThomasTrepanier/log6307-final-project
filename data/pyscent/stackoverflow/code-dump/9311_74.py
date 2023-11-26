def seqIncCheck(lst):
    temp = lst[0]
    for i in range(1,len(lst)):
        if lst[i] > temp:
           temp = lst[i]
           continue
        else:
           return False
    return True
