def primePart(N):
    return N%2==0 or all((N-2)%p for p in range(3,int(N**0.5)+1,2))

primePart(3432)  # True

primePart(37+2)  # True

primePart(13+41) # True

primePart(123)   # False
    
