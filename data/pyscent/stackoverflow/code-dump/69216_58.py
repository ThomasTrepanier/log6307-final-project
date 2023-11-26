import re
from typing import Optional

from dataclasses import dataclass, fields


@dataclass(frozen=True)
class TestClass:
    required_field_1: str
    required_field_2: int
    optional_field: Optional[str]


def get_optional_fields(klass):
    class_fields = fields(klass)
    for field in class_fields:
        if (
            hasattr(field.type, "__args__")
            and len(field.type.__args__) == 2
            and field.type.__args__[-1] is type(None)
        ):
            # Check if exactly two arguments exists and one of them are None type
            yield field.name


print(list(get_optional_fields(TestClass)))
