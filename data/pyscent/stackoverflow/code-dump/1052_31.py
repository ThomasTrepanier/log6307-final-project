@dataclasses.dataclass(frozen=True)
class SimpleClass:
    a: int

    @temp_unfreeze_for_postinit
    def __post_init__(self, adder):
        self.b = self.a + adder
