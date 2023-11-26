@dataclass
class Specs2:
    a: str
    b: str
    c: str

    def __post_init__(self):
        if self.b is None:
            self.b = 'Bravo'
        if self.c is None:
            self.c = 'Charlie'
