def nextpow10(n):
    p = round(math.log10(n))
    r = 10 ** p
    if r < n:
        r = 10 ** (p+1) 
    return r;
