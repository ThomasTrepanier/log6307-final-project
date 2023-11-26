import enum

class TestMeta(enum.EnumMeta):
    def __call__(cls, value, names=None, *, module=None, qualname=None, type=None, start=1):
        if names is not None:
            # the enum is being constructed via the functional syntax
            return super().__call__(value, names=names, module=module, qualname=qualname, type=type, start=start)

        try:
            # attempt to get an enum member
            return super().__call__(value, names=names, module=module, qualname=qualname, type=type, start=start)
        except ValueError:
            # no such member exists, but we don't care
            return value

class Test(enum.Enum, metaclass=TestMeta):
    A = 5
    B = 6    

print(Test(5), Test(6), Test(7))
