a=A()
a.attr='something'

def f(self):
    return 0

a.fun=f.__get__(a)
a.fun()
# 0
