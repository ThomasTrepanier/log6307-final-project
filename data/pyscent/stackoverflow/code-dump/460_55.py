from dataclasses import dataclass
from pydantic import validate_arguments


@validate_arguments
@dataclass
class Test:
    value: int

