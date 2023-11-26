from __future__ import annotations
from dataclasses import field, fields, dataclass

@dataclass()
class Record:
    name: str
    address: str
    zip: str = field(default=None)  # won't fail if dictionary doesn't have a zip key

    @classmethod
    def create_from_dict(cls, dict_) -> Record:
        class_fields = {f.name for f in fields(cls)}
        return Record(**{k: v for k, v in dict_.items() if k in class_fields})
