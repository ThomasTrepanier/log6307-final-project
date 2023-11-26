def combinations(aList):
    yield []
    for i,v in enumerate(aList,1):
        yield from ([v]+c for c in combinations(aList[i:]))
    

for combo in combinations([1,2,3]): print(combo)

[]
[1]
[1, 2]
[1, 2, 3]
[1, 3]
[2]
[2, 3]
[3]
