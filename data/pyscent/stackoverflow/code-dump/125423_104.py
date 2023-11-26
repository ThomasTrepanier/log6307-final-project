from dataclasses import dataclass, asdict
from enum import Enum
from typing import Union


@dataclass
class Foobar:
    name:str
    template: Union["FoobarEnum", str]
    def __post_init__(self):
        self.template = self.template.value

class FoobarEnum(Enum):
    FIRST = "foobar"
    SECOND = "baz"

foobar = Foobar(name="John", template=FoobarEnum.FIRST)
print(asdict(foobar))
