class TransactionType(Enum):

    IN = "IN"
    OUT = "OUT"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)

class TransactionStatus(Enum):

    INITIATED = "INITIATED"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    ERROR = "ERROR"

    @classmethod
    def choices(cls):
        print(tuple((i.value, i.name) for i in cls))
        return tuple((i.value, i.name) for i in cls)
