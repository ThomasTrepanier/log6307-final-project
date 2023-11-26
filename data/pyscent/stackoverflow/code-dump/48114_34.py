from dataclasses import dataclass, field

@dataclass
class SomeClass:
    """
    """

    some_list: list = field(default_factory=lambda: ["your_values"])
