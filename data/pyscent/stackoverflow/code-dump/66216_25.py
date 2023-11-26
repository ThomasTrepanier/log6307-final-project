class Parent(BaseModel):
    id: int
    name: str
    email: str

class ParentUpdate(Parent): ## Note that this inherits 'Parent' class (not BaseModel)
    id: Optional[int]  # this will convert id from required to optional
