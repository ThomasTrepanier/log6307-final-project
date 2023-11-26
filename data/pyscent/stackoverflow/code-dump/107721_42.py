def foo(x, y):
    if passed_positionally(y):
        raise Exception("You need to pass 'y' as a keyword argument")
    else:
        process(x, y)
