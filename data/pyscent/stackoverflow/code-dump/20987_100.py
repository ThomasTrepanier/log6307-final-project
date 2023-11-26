L = ['f','g','p','a','p','c','b','q','z','n','d','t','q']

def sort_func(x):
    priority = {'p': 0, 'q': 2}
    return priority.get(x, 1), x

res = sorted(L, key=sort_func)

print(res)

['p', 'p', 'a', 'b', 'c', 'd', 'f', 'g', 'n', 't', 'z', 'q', 'q']
