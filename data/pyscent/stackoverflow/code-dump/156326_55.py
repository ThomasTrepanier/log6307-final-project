@si.inject('foo', 'PI', 'uppercase')
def bar(a, b, c, uppercase: UpperCaseRepresentation, **kwargs):
    """
    You can specify dependencies as keyword arguments and add typehint annotation.
    """
    UpperCase, foo = kwargs['UpperCase'], kwargs['foo']
    print(uppercase('abc')) # ABC
    print(PI) # 3.141592653
    print(foo(a, b, c, 4, 5)) # = 15

bar(1, 2, 3)
