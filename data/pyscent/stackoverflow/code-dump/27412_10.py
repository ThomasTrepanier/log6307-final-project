class Shape:

    def __init__(self, x: float, y: float, name="default name", verbose=False):
        self.x = x
        self.y = y
        self.name = name
        if verbose:
            print("Initialized:", self)

    def __repr__(self):
        return f"{type(self).__name__}(x={self.x},y={self.y},name={self.name})"

class Circle(Shape):

    def __init__(self, x: float, y: float, r: float, **kwargs):
        self.r = r
        super().__init__(x, y, **kwargs)

    def __repr__(self):
        return f"{type(self).__name__}(r={self.r},x={self.x},y={self.y},name={self.name})"

