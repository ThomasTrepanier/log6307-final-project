from aenum import Enum, extend_enum

class Foo(Enum):
    _order_ = 'A B C'   # because Python 2 does not keep order
    A = 1
    B = 2
    C = 3

    def __str__(self):
        return self.name

    @classmethod
    def _missing_(cls, value):
        extend_enum(cls, str(value), (value, ))
        return list(cls)[-1]
