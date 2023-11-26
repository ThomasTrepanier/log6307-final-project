from dataclasses import dataclass, fields

@dataclass()
class Test:
    value: int

    def __post_init__(self):
        for field in fields(self):
            setattr(self, field.name, field.type(getattr(self, field.name)))
