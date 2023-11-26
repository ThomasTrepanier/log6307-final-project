L = [1,2,3,4,1,1,1,2,3,4]
n = 3
def consecutive (L,n):
    c = 0
    for i in L:
        if i == 1:
            c += 1
        else:
            c = 0
        if c >= n:
            return True
    return False


print(consecutive(L,n))
