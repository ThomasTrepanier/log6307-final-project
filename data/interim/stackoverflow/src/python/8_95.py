@kwargs_decorator({'bar': 1})
def foo(**kwargs):
    print(kwargs['bar'])

foo() # prints 1
