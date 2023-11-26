def consecutive (L,n, elem):
    count = 0
    for i in range(len(L)):
        if L[i] == elem:
            count = count + 1
            if count >= n:
                return True
        else: # L[i] != elem
            count = 0
    return False
