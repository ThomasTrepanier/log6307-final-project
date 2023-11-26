def f(name):
    print(name or 'Hello Guest')

def A(name=None):    
    f(name)

A()
Out: "Hello Guest"

A("Hello World")
Out: "Hello World"
