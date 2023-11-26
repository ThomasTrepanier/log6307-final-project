@dataclass
class Person:
    name: str
    age: float

    def __setattr__(self, name, value):
        if name == 'age':
            assert value > 0, f"value of {name} can't be negative: {value}"
        self.__dict__[name] = value
