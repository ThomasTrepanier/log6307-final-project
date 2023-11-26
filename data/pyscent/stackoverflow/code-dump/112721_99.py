import math
def steps2Zero(N):
    if N < 2: return N
    d = int(math.log(N+2,2))-1
    s = int(N >= 3*2**d-2)
    return 2*d+s
