si = ServiceInjector()

# use func.__name__, registering func
@si.register()
def foo(*args):
    return sum(args)
