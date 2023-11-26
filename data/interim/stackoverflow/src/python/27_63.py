def listToListOfProds(orig):
    curr = 1
    newList = []
    for item in orig:
        curr *= item
        newList.append(curr)
    return newList

print(listToListOfProds([1, 2, 3, 4, 5]))
