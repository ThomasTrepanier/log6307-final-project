def solve(A):
    x = ['a', 'e','i','o', 'u', 'A', 'E', 'I', 'O', 'U']
    y = []
    z = len(A)
    for n,i in enumerate(A):
        if i in x:
            m = z
            while m > n:
                y.append(A[n:m])
                m -= 1
    if y:
        return len(y)%10003
    else:
        return 0
