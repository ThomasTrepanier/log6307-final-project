def summer69(a):
    for z in a:
        if z==6 and 9 in a:
           x=a.index(6)
           y=a.index(9)
           del a[x:y+1]
           t= sum(a)
        else:
           t=sum(a)
    return t
