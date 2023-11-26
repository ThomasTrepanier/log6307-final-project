class MyStrEnum(str, Enum):

    OK     = 'OK'
    FAILED = 'FAILED'

    def __str__(self) -> str:
        return self.value
