def fibonacci(n):
    ls = []
    for i in range(0,n):
        if (i==0) or (i==1):
            n=1
            ls.append(n)
        elif i>=2:
            ls.append(ls[-1]+ls[-2])
            n=ls[-2] + ls[-3]
    print(n)


while(True):
    x = int(input())
    fibonacci(x)
