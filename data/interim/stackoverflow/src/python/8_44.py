def cycles(indices):

    sub =[]
    i=0
    result = []
    remaining = indices[:]

    while remaining:
        i = indices[i]
        if(i in sub):
            remaining = [ a for a in remaining if a not in sub]
            result.append(sub)
            sub = []
            if remaining:
                i=remaining[0]

        sub.append(i)
    return result

r = cycles([2, 0, 1, 4, 3, 5])
print(r)
#[[2, 1, 0], [4, 3], [5]]

r = cycles([0,1,2,3,4,5])
print(r)
#[[0], [1], [2], [3], [4], [5]]
