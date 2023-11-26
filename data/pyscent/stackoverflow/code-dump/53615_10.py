from dataclasses import dataclass

@dataclass
class XY:
    "2d point"
    x: float or int
    y: float or int

points = [XY(1, 2), XY(3, 4), XY(5, 6), XY(7, 8)]
data_dict = dict(zip(('x', 'y'), zip(*(vars(p).values() for p in points))))

print(data_dict)
