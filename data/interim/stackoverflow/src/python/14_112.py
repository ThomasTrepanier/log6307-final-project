def accepts(*types):
    """
    Enforce parameter types for function
    Modified from https://stackoverflow.com/questions/15299878/how-to-use-python-decorators-to-check-function-arguments
    :param types: int, (int,float), if False, None or [] will be skipped
    """
    def check_accepts(f):
        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                if t:
                    assert isinstance(a, t), \
                           "arg %r does not match %s" % (a, t)
            return f(*args, **kwds)
        new_f.func_name = f.__name__
        return new_f
    return check_accepts
