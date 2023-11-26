lst = [4, 5, 6, 7, 8, 9]

def summer_69(lst):
    s = 0
    while lst:
        i = lst.pop()
        if i == 9:
            while i!=6:
                i = lst.pop()
        else:
            s += i
    return s

print(summer_69(lst))
