def fib_acc(n, a, b):
    if n == 1:
        return (a, b)
    return lambda: fib_acc(n - 1, (a+b) % 997, (a+2*b) % 997)

def fib(n):
    x = fib_acc(n, 1, 2)
    while callable(x):
        x = x()
    return x

if __name__=='__main__':
    print(fib(50000)[0])
