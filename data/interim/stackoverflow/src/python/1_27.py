class Choices(int, Enum):
    anne = 1
    ben = 2
    charlie = 3
    dave = 4

    @classmethod
    def __get_validators__(cls):
        cls.lookup = {v: k.value for v, k in cls.__members__.items()}
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return cls.lookup[v]
        except KeyError:
            raise ValueError('invalid value')

class Model(BaseModel):
    choice: Choices

debug(Model(choice='charlie'))
