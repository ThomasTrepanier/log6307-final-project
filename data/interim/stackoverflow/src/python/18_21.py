from dataclasses import dataclass
from typing import Optional

@dataclass
class Toy1:
    color: str
    age: int
    field3: Optional[str] = None
    fielg4: Optional[str] = None
    field5: Optional[str] = None

    def __init__(self, color:str, age: int) -> None:
        self.color = color
        self.age = age

toy1 = Toy('red', 2)
