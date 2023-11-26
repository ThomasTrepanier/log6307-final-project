@dataclass(init=False)
class Config:
    VAR_NAME_1: str
    VAR_NAME_2: str

    def __init__(self, **kwargs):
        names = set([f.name for f in dataclasses.fields(self)])
        for k, v in kwargs.items():
            if k in names:
                setattr(self, k, v)
