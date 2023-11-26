import timeit
from enum import Enum, EnumMeta
from random import randint


class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True    


class BaseEnum(Enum, metaclass=MetaEnum):
    pass


class Action(BaseEnum):
    A = 1
    B = 2
    C = 3
    D = 4
    
    def is_action(obj):
        try:
            Action(obj)
        except ValueError:
            return False
        return True

repeat, N = 100, 10000
t_is_x = timeit.repeat(stmt="Action.is_action(i)", setup='from random import randint; i = randint(1, 8)', number=N, repeat=repeat, globals=globals())
t_meta = timeit.repeat(stmt="i in Action", setup='from random import randint; i = randint(1, 8)', number=N, repeat=repeat, globals=globals())
t_valuemap = timeit.repeat(stmt="i in Action._value2member_map_", setup='from random import randint; i = randint(1, 8)', number=N, repeat=repeat, globals=globals())

print(f"Time for is_x: {min(t_is_x)}")
print(f"Time for meta: {min(t_meta)}")
print(f"Time for value map: {min(t_valuemap)}")
