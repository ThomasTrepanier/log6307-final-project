class ModelBase(pydantic.BaseModel):
  a: int
  b: str


class ModelCreate(ModelBase):
  pass

# Make all fields optional
@make_optional()
class ModelUpdate(ModelBase):
  pass
