mylist = [['a','b','c',''],['c','e','f'],['c','g','h']]


def combine(x, y):
    for m in y:
        if not m in x:
            x.append(m)
    return(x)

result = [] 

for x in mylist:

    if x[len(x) - 1] == '':

        m = x[len(x) - 2]
        for y in mylist:
            if y[0] == m:
                result.append(combine(x[0:len(x)-2], y))

print(result)
