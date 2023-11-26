def consecutive (L,n):
    if len(L) < 1:
        return False
    if n <= 1:
        return True

    # at this point n >= 2
    elem = L[0]
    count = 1
    # so far, we have seen one copy of `elem`

    for i in range(1, len(L)):
        if L[i] == elem:
            count = count + 1
            if count >= n:
                return True
        else: # L[i] != elem
            elem = L[i]
            count = 1
    return False
