def reverse(n):
    r = 0
    while n != 0:
        r = r*10 + int(n%10)
        n = int(n/10)
    return r

def f(n):
    for i in range(n + 1):
        if i + reverse(i) == n:
            return True
    return False

print('Yes' if f(101) else 'No')
#Yes
