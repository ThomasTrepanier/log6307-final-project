class CustomReprFunc:

    def __init__(self, f, custom_repr):
        self.f = f
        self.custom_repr = custom_repr

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

    def __repr__(self):
        return self.custom_repr(self.f)


def set_repr(custom_repr):
    def set_repr_decorator(f):
        return CustomReprFunc(f, custom_repr)
    return set_repr_decorator


@set_repr(lambda f: f.__name__)
def func(a):
    return a


print(repr(func))
