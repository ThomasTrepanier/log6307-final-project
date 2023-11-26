l = ['f','g','p','a','p','c','b','q','z','n','d','t','q']

def key(c):
    if c == 'q':
        return (2, c)
    elif c == 'p':
        return (0, c)
    return (1, c)


result = sorted(l, key=key)
print(result)
