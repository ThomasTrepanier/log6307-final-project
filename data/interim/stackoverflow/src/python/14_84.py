from enum import Enum

class BaseEnum(Enum):
    def __new__(cls, *args):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        obj.display_name = args[1]
        return obj

    @classmethod
    def model_choices(cls):
        return [(cls.__members__[member].value, cls.__members__[member].display_name)
            for member in cls.__members__.keys()]
