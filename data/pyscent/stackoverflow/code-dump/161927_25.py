from itertools import combinations_with_replacement as cwr

def countways(l, target):
    for i in range(target):
        for j in cwr(l, i + 1):
            if sum(j) == target:
                print(j)

countways([1, 2, 3], 5)
