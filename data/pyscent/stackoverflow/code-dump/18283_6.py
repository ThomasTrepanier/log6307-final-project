a = [1,2,3,4]

def rep(s, l, ab):
    id = l.index(s)
    q = s
    del(l[id])
    l.insert(ab, q)
    return l

l = rep(a[0], a, 2)
print(l)
