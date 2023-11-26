def c_find(*roots):
    from sympy import Symbol
    x = Symbol('x')
    whole =1
    for root in roots:
        whole *=(x-root)
    print('f(x) =',whole.expand())
