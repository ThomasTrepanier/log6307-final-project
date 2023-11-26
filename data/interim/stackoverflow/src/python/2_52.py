def remdup(l):
    visited= []
    for i in range(len(l)-1, -1, -1):
        if l[i] in visited:
            l.pop(i)
        else:
            visited.append(l[i])
    print(l)

remdup([3,5,7,5,3,7,10])
#[5, 3, 7, 10]
