from dataclasses import dataclass, InitVar, field

@dataclass
class Shape:
    x: float
    y: float
    name: str = field(kw_only=True, default="default name")
    verbose: InitVar[bool] = field(kw_only=True, default=False)

    def __post_init__(self, verbose):
        if verbose:
            print("Initialized:", self)

@dataclass
class Circle(Shape):
    r: float
