sorted_ids=[1, 2, 4, 5, 8, 9, 10, 12, 13, 16, 17, 18, 20]

def arrange(inList):
    newList = []
    newList.append('T'+str(inList[0]))
    for i in range(1,len(inList)):
        diff = inList[i] - inList[i-1]
        if diff > 1:
            for d in range(diff-1):
                newList.append('V')
            newList.append('T'+str(inList[i]))
        else:
            newList.append('T'+str(inList[i]))
    return newList

print(arrange(sorted_ids))
