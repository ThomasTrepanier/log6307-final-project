def partition(num):
    """
    Return True if there exist primes x,y such that num = x + y.
    Else return False.
    """
    primelist = primes(num)
    for x in primelist:
        y= num-x
        # Note: num = x + y, thus need only check y prime
        if y in primelist:
            return True
    # If no such y is prime, not possible
    else:
        return False

def primes(num):
    """Return list of all primes less than num."""
    primelist=[]
    for i in range(2,num + 1):
        for p in range(2,i):
            if (i % p) == 0:
                break
        else:
            primelist.append(i)
    return primelist
