def listOfLists(n,lists=[]):
    lists.append([])
    if n == 1:   
        return

    listOfLists(n-1,lists)
    return lists

print (listOfLists(4))
