def findPQ(N):
    if not primePart(N): return
    if N%2: return 2,N-2
    skip,primes = {},{2}
    for p in range(3,N,2):
        if p in skip:
            prime = skip.pop(p)
            mult  = p + 2*prime
            while mult in skip: mult += 2*prime
            if mult <= N: skip[mult] = prime
        else:
            if 2*p>=N and N-p in primes: return p,N-p
            if p*p<=N: skip[p*p]=p
            if 2*p<=N: primes.add(p)
