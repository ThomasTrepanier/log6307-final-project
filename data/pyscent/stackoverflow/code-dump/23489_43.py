def H(n):
    if n == 1:
        return 1
    else:
        return 2*H(n-1)+1
