class Variable:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @property
    def value(self):
        print(self._name, 'get', self._value)
        return self._value

    @value.setter
    def value(self):
        print(self._name, 'set', self._value)
        self._value = value

a = Variable('a', 1)
b = Variable('b', 2)

a.value, b.value = b.value, a.value
