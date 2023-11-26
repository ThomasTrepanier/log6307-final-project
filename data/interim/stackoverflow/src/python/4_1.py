from enum import Enum
from types import DynamicClassAttribute

class MixedCaseEnum(Enum):
    @DynamicClassAttribute
    def name(self):
        return self._name_.title()

class Rank(MixedCaseEnum):
    KING = 13

print(Rank.KING.name) # outputs 'King'
print(Rank.KING.value) # outputs 13
