import dataclasses

@dataclasses.dataclass
class Test:
    value : int

    def __post_init__(self):
        self.value = int(self.value)
