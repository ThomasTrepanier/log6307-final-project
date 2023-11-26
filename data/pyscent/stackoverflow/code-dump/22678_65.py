@default_kwargs(a='a', b='b', d='d')
def f(x, a, b, *args, c='c', d='not d', **kwargs):
    print(f'x = {x}')
    print(f'a = {a}')
    print(f'b = {b}')
    for idx, arg in enumerate(args):
        print(f'arg{idx} = {arg}')
    print(f'c = {c}')
    for key, value in kwargs.items():
        print(f'{key} = {value}')

f(1)
f(1, 2)
f(1, b=3)
f(1, 2, 3, 4)
f(1, 2, 3, 4, 5, c=6, g=7)
