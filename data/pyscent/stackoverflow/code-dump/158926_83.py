def func(x):
    d = {'edu':'e','com':'m','org':'o'}
    return d.get(x.split('.')[-1],'z')

print(sorted(urls, key=func))
