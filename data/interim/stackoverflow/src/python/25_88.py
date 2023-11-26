def f(name='Hello Guest'):
    print(name or inspect.signature(f).parameters['name'].default)


def A(name=None):    
    f(name)

A()
# Hello Guest
