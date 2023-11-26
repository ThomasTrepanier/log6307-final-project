def repeatedString(s,n):
    i = 0
    c = 0
    for i in s:
        if i == 'a':
            c += 1

    q = int(n / len(s)) #Finding the quotient 
    r = int(n % len(s)) #Finding the remainder
    if r == 0: 
        c *= q 

    else:
        x = 0
        for i in range(r):
            if s[i] == 'a':
                x += 1
        c = c*q + x

    return int(c)

s = input()
n = int(input())
print(repeatedString(s,n))
