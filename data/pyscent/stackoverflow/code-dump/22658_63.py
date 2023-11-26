@kwargs_decorator(a='a', b='b')
def f(x, a, b):
    print(f'x = {x}')
    print(f'a = {a}')
    print(f'b = {b}')

f(1, 2)
