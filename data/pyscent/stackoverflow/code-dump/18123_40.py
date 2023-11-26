def combinations(aList):
    return [[]] + [ [v]+c for i,v in enumerate(aList,1) 
                          for c   in combinations(aList[i:]) ]

print( combinations([1,2,3]) )

[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
