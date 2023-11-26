def pow(n):
    global calls
    calls+=1
    """Return 2**n, where n is a nonnegative integer."""
    if n == 0:
        return 1
    x = pow(n//2)
    if n%2 == 0:
        return x*x
    return 2*x*x

def steppow(n):
    global calls
    calls=0
    pow(n)
    return calls

sx = [math.pow(10,n) for n in range(1,11)]
sy = [steppow(n)/math.log(n) for n in sx]
print(sy)
