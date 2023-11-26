def factors(n):
    factlist = []
    for i in range(1,n+1):
        # Since factors of 2 cannot be primes, we ignore them.
        if n%i==0 and i%2!=0:
            factlist.append(i)
    return factlist

def isprime(n):
    return(factors(n)==[1,n])

def preimesupto(n):
    primelist = []
    if n>=2:
        primelist.append(2)
    for i in range(n):
        if isprime(i):
            primelist.append(i)
    return primelist

def primepartition(n):
    if n<0:
        return False
    primelist = preimesupto(n)
    for i in primelist:
        j = n-i
        if j in primelist:
            return True
    else:
        return False
