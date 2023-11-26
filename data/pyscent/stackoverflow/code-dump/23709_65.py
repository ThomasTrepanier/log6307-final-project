list =[1,1,1,3,4,5,5,6,7]

def Duplicate(func,data):
    start = -1
    y = []
    while True:
        try:
            x = func.index(data,start+1)
        except ValueError:
            break
        else:
            y.append(x)
            start = x
    return y

from functools import partial
New= partial(Duplicate, list)

for a in list:
    print(a, New(a))
