import numbers

class Complex:
    def __add__(self, other):
        if isinstance(self, Complex):
            ...
        elif isinstance(other, numbers.Real):
            ...
        else:
            raise TypeError

    def __radd__(self, other):
        return self + other
