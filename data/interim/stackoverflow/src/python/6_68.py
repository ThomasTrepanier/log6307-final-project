def values():
    yield 'o'
    for i in range(3, 10, 2):
        yield ' '.join('*' * i)
    yield from '||'

for v in values():
    print('{:~^17}'.format(v))
