def findPQ(N):
    if not primePart(N): return
    if N%2: return 2,N-2
    isPrime = [0]+[1]*N
    for p in range(3,N,2):
        if not isPrime[p]: continue
        if 2*p>=N and isPrime[N-p]: return p,N-p
        isPrime[p*p::p] = [0]*len(isPrime[p*p::p])
