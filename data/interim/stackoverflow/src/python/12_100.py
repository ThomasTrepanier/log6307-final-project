from math import pi

class Cylinder:
    _independent = {"length", "radius", "density"}
    _dependent = {"volume", "mass"}

    def __init__(self, radius, length, density):
        self._radius = radius
        self._length = length
        self._density = density
        self._volume = None
        self._mass = None

    def __setattr__(self, name, value):
        if name in self._independent:
            name = f"_{name}"
            for var in self._dependent:
                super().__setattr__(f"_{var}", None)
        if name in self._dependent:
            print("Cannot set dependent variable!")
            return
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
