def getfunc(i):
    return lambda: i

funcs = []
for i in range(5):
    funcs.append(getfunc(i))

for item in funcs:
    print(item())
