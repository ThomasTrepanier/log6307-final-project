class Shape:
    def __init__(x: float, y: float):
        self.x = x
        self.y = y


class Circle(Shape):
    def __init__(x: float, y: float, radius: float):
        super().__init__(x=x, y=y)
        self.radius = radius


# The expectation is that this should work with all instances of `Shape`
def move_shape(shape: Shape, x: float, y: float):
    shape.x = x
    shape.y = y
