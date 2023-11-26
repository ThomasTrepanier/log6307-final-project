def listOfLists(n):
    lists = [[]]
    if n <= 1:
        return lists
    else:
        return lists + listOfLists(n-1)
