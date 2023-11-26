def factors(n):
    factorslist = []
    for i in range(1, n+1, 1):
        if n % i == 0:
            factorslist.append(i)
    return(factorslist)    

def prime(n):
    if factors(n) == [1, n] and n > 1:
        return(True)

def primelist(n):
    primenolist = []
    for i in range(1, n+1, 1):
        if prime(i) == True:
            primenolist.append(i)
    return(primenolist)

def primepartition(m):
    if m > 0:
        primenolist = primelist(m)
        checklist = []
        for p in primenolist:
            q = m - p
            if q in primenolist and p > 0 and q > 0:
                checklist.append((p,q))
        if len(checklist) > 0:
            return(True)
        else:
            return(False)
    else:
        return(False)
