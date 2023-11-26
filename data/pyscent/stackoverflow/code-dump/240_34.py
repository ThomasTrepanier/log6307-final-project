class IntConversionDescriptor:

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        setattr(instance, self._name, int(value))


@dataclass
class Test:
    value: IntConversionDescriptor = IntConversionDescriptor()
