def foo(bar = 1):
    print('bar:', type(bar), bar)

s = 'bar = 170'
d = {k.strip(): int(v.strip()) for k, v in [s.split('=', 1)]}
print('d:', type(d), d)
foo(**d)
