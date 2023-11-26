#enums.py
class TransactionType(Enum):
    IN = "IN"
    OUT = "OUT"

    @classmethod
    def choices(cls):
        return [(i, i.value) for i in cls]
