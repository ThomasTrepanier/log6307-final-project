from pydantic import BaseModel, create_model
from typing import Optional

def make_optional(baseclass):
    # Extracts the fields and validators from the baseclass and make fields optional
    fields = baseclass.__fields__
    validators = {'__validators__': baseclass.__validators__}
    optional_fields = {key: (Optional[item.type_], None) for key, item in fields.items()}
    return create_model(f'{baseclass.__name__}Optional', **optional_fields, __validators__=validators)

class Parent(BaseModel):
    id: int
    name: str
    email: str

ParentUpdate = make_optional(Parent)
