from enum import Enum
import functools


@functools.total_ordering
class MyEnum(Enum):
    A = "apple"
    C = "cherry"
    B = "banana"

    def __eq__(self, other):
        if isinstance(other, MyEnum):
            return (
                self._member_names_.index(self.name) ==
                self._member_names_.index(other.name)
            )
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, MyEnum):
            return (
                self._member_names_.index(self.name) >
                self._member_names_.index(other.name)
            )
        return NotImplemented


print(MyEnum.A < MyEnum.B)  # True
print(MyEnum.B >= MyEnum.C)  # True
print(MyEnum.C < MyEnum.A)  # False
