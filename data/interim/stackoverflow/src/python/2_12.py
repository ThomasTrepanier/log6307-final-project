def get_new(l):
    N = l.copy()
    for a in range(len(N)):
        for b in N[a].keys():
            if b in ['a','b']:
                i = 1
                while N[a][b]: # while N[a][b] is not empty.
                    key = str(b) + '_' + str(i)
                    i += 1
                    N[a][key] = N[a][b].pop(0)
                del N[a][b]
    
    return N
