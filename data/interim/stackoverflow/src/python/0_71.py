@dataclasses.dataclass
class Test:
    value: int

    def __post_init__(self):
        if not isinstance(self.value, int):
            raise ValueError('value not an int')
            # or self.value = int(self.value)
