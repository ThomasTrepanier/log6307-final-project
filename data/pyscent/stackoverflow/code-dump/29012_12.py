from dataclasses import dataclass, InitVar, field

@dataclass
class DCShape:
    x: float
    y: float
    scale: InitVar[float] = field(kw_only=True, default=1)
    name: str = field(kw_only=True, default="default name")
    verbose: InitVar[bool] = field(kw_only=True, default=False)

    def __post_init__(self, scale, verbose):
        self.x = scale * self.x
        self.y = scale * self.y
        if verbose:
            print("Initialized:", self)

@dataclass
class DCCircle(DCShape):
    r: float

    def __post_init__(self, scale, verbose):
        self.r = scale * self.r
        super().__post_init__(scale, verbose)
