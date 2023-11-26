def comb(arrs, i=0, numbs=[]):
    if i == len(arrs):
        print(*numbs)
        return
    for j in arrs[i]:
        comb(arrs, i + 1, numbs + [j])

arrs = [[1,2,3],[3,4,5],[5,6,7,8]]
comb(arrs)
