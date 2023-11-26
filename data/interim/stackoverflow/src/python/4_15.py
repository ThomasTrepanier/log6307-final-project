from dataclasses import dataclass, astuple

@dataclass
class XY:
    "2d point"
    x: float | int
    y: float | int
    def __iter__(self):
        return iter(astuple(self))

points = [XY(1,2), XY(3,4), XY(5,6), XY(7,8)]
xs, ys = zip(*points)
