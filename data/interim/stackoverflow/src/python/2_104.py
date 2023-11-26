def primepartition0(m):
    primelist=[]
    if m<0:
        return False
    else:
        for i in range(2,m + 1):
            for p in range(2,i):
                if (i % p) == 0:
                    break
            else:
                primelist.append(i)

        for x in primelist:
            for y in primelist:
                if x != y and x+y == m:
                    return True
        return False   
