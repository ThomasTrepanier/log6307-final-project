from dataclasses import dataclass
from typing import Optional, Union

@dataclass
class A:
    foo : Optional[int] = None
    bar : int|None = None
    baz : Union[int, float, None] = None
    x : int = 1

a=A()
assert field_is_optional(type(a), "foo")
assert field_is_optional(type(a), "bar")
assert field_is_optional(type(a), "baz")
assert field_is_optional(type(a), "x") == False
