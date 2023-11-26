def solution(data, n):
    lis=[]
    lis2=[]
    a=''
    for i in data:
        if i not in lis2 and data.count(i)<=n and n>0:
            lis2.append(str(i))
            lis2.append(',')
        else:
            lis.append(i)
            break
    for i in lis2:
       a+=i
    return a[:-1]
