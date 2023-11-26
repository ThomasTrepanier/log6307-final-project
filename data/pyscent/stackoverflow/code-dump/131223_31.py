@dataclass
class Test(metaclass=field_property_support):
    my_int: int
    name: str
    my_bool: bool = True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        print(f'Setting name to: {val!r}')
        self._name = val
