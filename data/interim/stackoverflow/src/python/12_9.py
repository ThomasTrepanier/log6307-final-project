class Shape:
    def __init__(x: float, y: float, colour: str = "black"):
        self.x = x
        self.y = y
        self.colour = colour 


class Circle(Shape):
    def __init__(x: float, y: float, radius: float, **kwargs):
        super().__init__(x=x, y=y, **kwargs)
        self.radius = radius


def move_shape(shape: Shape, x: float, y: float):
    shape.x = x
    shape.y = y


def colour_shape(shape: Shape, colour: str):
    shape.colour = colour
