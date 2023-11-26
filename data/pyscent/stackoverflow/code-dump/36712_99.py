from math import pi
# define the functions outside the class
def volfnc(length, radius):
    return length * pi * pow(radius,2)
def massfnc(volume, density):
    return volume * density

class Cylinder:
    volume = DependantAttribute('volume',volfnc, ('length','radius'))
    mass = DependantAttribute('mass',massfnc, ('volume','density'))

    def __init__(self, radius, length, density):

        self.radius = radius
        self.length = length
        self.density = density

        # the dependent attributes must be set in __init__
        self.volume = volfnc(length,radius)
        self.mass = massfnc(self.volume,density)


c = Cylinder(1,1,1)
d = Cylinder(1,2,1)
