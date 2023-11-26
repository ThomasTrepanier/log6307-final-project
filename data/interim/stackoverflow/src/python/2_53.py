def remdup(l):
    i = 0
    while i < len(l):
        v = l[i]
        scan = i + 1
        while scan < len(l):
            if l[scan] == v:
                l.remove(v)
                scan -= 1
                i -= 1
            scan += 1
        i += 1

l = [3,5,7,5,3,7,10]
remdup(l)
print(l)
