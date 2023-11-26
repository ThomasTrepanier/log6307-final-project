from dataclasses import dataclass, asdict
from enum import Enum


@dataclass
class Foobar:
  name: str
  template: "FoobarEnum"


class FoobarEnum(Enum):
  FIRST = "foobar"
  SECOND = "baz"


def custom_asdict_factory(data):

    def convert_value(obj):
        if isinstance(obj, Enum):
            return obj.value
        return obj

    return dict((k, convert_value(v)) for k, v in data)


foobar = Foobar(name="John", template=FoobarEnum.FIRST)

print(asdict(foobar, dict_factory=custom_asdict_factory))
# {'name': 'John', 'template': 'foobar'}
