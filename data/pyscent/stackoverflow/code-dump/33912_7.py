from inspect import signature, Signature
from itertools import chain
from collections import OrderedDict


def make_signature(subclass, superclass):
    """Returns a signature object for the subclass constructor's __signature__ attribute."""
    sub_params = signature(superclass.__init__).parameters
    sup_params = signature(subclass.__init__).parameters
    mixed_params = OrderedDict(chain(sub_params.items(), sup_params.items()))
    mixed_signature = Signature(parameters=mixed_params.values())
    return mixed_signature


class Shape:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Circle(Shape):
    def __init__(self, radius: float, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius


Circle.__signature__ = make_signature(Circle, Shape)

if __name__ == "__main__":
    help(Circle)  # Circle(self, x: float, y: float, radius: float, **kwargs) ...
