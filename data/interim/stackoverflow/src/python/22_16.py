from dataclasses import dataclass
import re
from enum import Enum


class Descriptor:
    def __init__(self, type, validators=(), **kwargs):
        self.type = type
        self.default = kwargs.get("default")
        self.validators = validators
        self.kwargs = kwargs

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if not instance:
            return self
        # return instance.__dict__[self.name]
        return instance.__dict__.get(self.name, self.default)

    def __delete__(self, instance):
        del instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value, Descriptor):
            value = self.default
        else:
            if not isinstance(value, self.type):
                raise TypeError(
                    f"{self.name!r} VALUES MUST BE TYPE {self.type!r} NOT {type(value)}!"
                )
            switch = {
                "POSITIVE": self.val_positive,
                "BETWEEN": self.val_between_values,
                "MAXMINZISE": self.val_between_sizes,
                "SIZE": self.val_size,
                "EMAIL": self.val_email,
                "NUMBER": self.val_number,
                "ONEOF": self.val_one_of,
            }
            for validator in self.validators:
                if validator in switch:
                    switch[validator](value)
        instance.__dict__[self.name] = value

    def val_positive(self, value: int | float):
        if value <= 0:
            raise ValueError(f"VALUE IS NOT VALID FOR {self.name!r} MUST BE POSITIVE")

    def val_between_values(self, value: int | float):
        maxval = self.kwargs.get("maxval")
        if maxval is not None:
            if not isinstance(maxval, int) or isinstance(maxval, float):
                raise TypeError(
                    f"MAX VALUE MUST BE TYPE INTEGER OR FLOAT NOT {type(value)}!"
                )
            if value > maxval:
                raise ValueError(
                    f"VALUE IS NOT VALID FOR {self.name!r} MUST BE GREATER THAN {maxval}"
                )
        minval = self.kwargs.get("minval")
        if minval is not None:
            if not isinstance(minval, int) or isinstance(maxval, float):
                raise TypeError(
                    f"MIN VALUE MUST BE TYPE INTEGER OR FLOAT NOT {type(value)}!"
                )
            if value < minval:
                raise ValueError(
                    f"VALUE IS NOT VALID FOR {self.name!r} MUST BE LESS THAN {minval}"
                )

    def val_between_sizes(self, value: int):
        maxsize = self.kwargs.get("maxsize")
        if maxsize is not None:
            if not isinstance(maxsize, int):
                raise TypeError(f"MAX VALUE MUST BE TYPE INTEGER NOT {type(value)}!")
            if len(value) > maxsize:
                raise ValueError(
                    f"VALUE IS NOT VALID FOR {self.name!r} MUST BE GREATER THAN {maxsize}"
                )
        minsize = self.kwargs.get("minsize")
        if minsize is not None:
            if not isinstance(minsize, int):
                raise TypeError(f"MIN VALUE MUST BE TYPE INTEGER NOT {type(value)}!")
            if len(value) < minsize:
                raise ValueError(
                    f"VALUE IS NOT VALID FOR {self.name!r} MUST BE LESS THAN {minsize}"
                )

    def val_size(self, value: str):
        length = self.kwargs.get("size")
        if length is None:
            raise ValueError("LEN NOT DEFINED")
        if len(value) > length:
            raise ValueError(
                f"VALUE IS NOT VALID FOR {self.name!r} THE LIMIT OF CHACRTERS IS {length}"
            )

    def val_email(self, value: str):
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.fullmatch(regex, value):
            raise ValueError("MAIL NOT VALID")

    def val_number(self, value: str):
        regex = "[0-9]+"
        if not re.match(regex, value):
            raise ValueError("STRING NUMBER NOT VALID")

    def val_one_of(self, value: str):
        posible_values = self.kwargs.get("posible_values")
        if posible_values is None:
            raise ValueError("POSIBLE VALUES NOT DEFINED")
        if not issubclass(posible_values, Enum):
            raise TypeError(f"POSIBLE VALUES MUST BE TYPE ENUM NOT {type(value)}!")
        values = [e.value for e in posible_values]
        if value not in values:
            raise ValueError(
                f"VALUE IS NOT VALID FOR {self.name!r} IS NOT PRESENT IN ARRAY {posible_values}"
            )
@dataclass
class Person():
   personid: str = Descriptor((str), ["SIZE"], size=8)
