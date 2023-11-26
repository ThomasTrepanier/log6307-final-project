def listOfLists(n, lists = []):
    if n > 0:
        lists.append([])
        return listOfLists(n-1, lists)
    else:
        return lists

print(listOfLists(4))
