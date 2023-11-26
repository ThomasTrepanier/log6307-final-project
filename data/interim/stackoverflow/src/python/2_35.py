ncalls=0
def fn(n):
    global ncalls
    ncalls +=1
    if n <= 1:
        return n
    elif n > 1 and n % 2 == 0:
        return fn(n/2)
    elif n > 1 and n % 2 > 0:
        return fn(3*n+1)

if __name__ == "__main__":
    n = 10
    print(f'fn({n}) = {fn(n)}, {ncalls} function call(s)')  
