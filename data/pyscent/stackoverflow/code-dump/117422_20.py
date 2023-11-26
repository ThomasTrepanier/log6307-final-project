def divisibleSumPairs(n, k, ar):
   
    import itertools
    
    return len([x for x in itertools.combinations(ar,r=2) if (x[0]+x[1])%k==0])
