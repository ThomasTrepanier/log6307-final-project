@partial_model
class Model(BaseModel):
    i: int
    f: float
    s: str


Model(i=1)
