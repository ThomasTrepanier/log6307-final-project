from itertools import chain
from math import pi

class Cylinder:

    _dependencies = {
        "length": ["volume"],
        "radius": ["volume"],
        "volume": ["mass"],
        "density": ["mass"]
    }
    _dependent_vars = set(chain(*list(_dependencies.values())))

    def __init__(self, radius, length, density):
        self._radius = radius
        self._length = length
        self._density = density
        self._volume = None
        self._mass = None

    def _reset_dependent_vars(self, name):
        for var in self._dependencies[name]:
            super().__setattr__(f"_{var}", None)
            if var in self._dependencies:
                self._reset_dependent_vars(var)

    def __setattr__(self, name, value):
        if name in self._dependent_vars:
            raise AttributeError("Cannot set this value.")
        if name in self._dependencies:
            self._reset_dependent_vars(name)
            name = f"_{name}"
        super().__setattr__(name, value)

    @property
    def volume(self):
        if self._volume is None:
            self._volume = self.length*pi*self.radius**2
            print("Volume calculated")
        return self._volume

    @property
    def mass(self):
        if self._mass is None:
            self._mass = self.volume*self.density
            print("Mass calculated")
        return self._mass

    @property
    def length(self):
        return self._length

    @property
    def radius(self):
        return self._radius

    @property
    def density(self):
        return self._density
