def f(s, c):
    s = s.lower()
    if s.count(c) != 2:
        return 0
    return s.index(c, mn+1)-s.index(c)+1
    

f('Saturday', 'a')
