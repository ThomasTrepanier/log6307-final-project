def f(name='Hello Guest'):
    print(name or f.__default__[0])


def A(name=None):    
    f(name)

A()
# Hello Guest
