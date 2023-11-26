def f1(n):
    if n <= 1:
        return 0
    else:
        isOdd = (n-1)%2==1
        return f1(n-1) + (n-1 if isOdd else 0)
