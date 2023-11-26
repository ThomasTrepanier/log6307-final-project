from pyfields import field
from typing import List

class Toy:
    color: str = field(doc="The toy's color, a string.")
    age: int = field(doc="How old is this Toy. An integer number of years.")
    field3: str = field(default='hello', check_type=True)
    field4: List[str] = field(default_factory=lambda obj: ['world'])
    field5: str = field(default=None, 
                        validators={'should be 1-character long': lambda x: len(x) == 1})

    def __init__(self, color, age):
        self.color = color
        self.age = age


t = Toy(color='blue', age=12)
print(t.field3 + ' ' + t.field4[0])
print(t.field5 is None)
t.field5 = 'yo'
