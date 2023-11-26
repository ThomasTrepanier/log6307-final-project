from operator import attrgetter
from dataclasses import dataclass

@dataclass
class XY:
    "2d point"
    x: float | int
    y: float | int

points = [XY(1,2), XY(3,4), XY(5,6), XY(7,8)]
xs, ys = map(list, zip(*map(attrgetter('x', 'y'), points)))
