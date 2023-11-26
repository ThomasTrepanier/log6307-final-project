from pydantic import BaseModel, create_model
from typing import Optional
from functools import lru_cache

@lru_cache(maxsize=None) # avoids creating many classes with same name
def make_optional(baseclass: Type[BaseModel]) -> Type[BaseModel]:
    # Extracts the fields and validators from the baseclass and make fields optional
    fields = baseclass.__fields__
    validators = {'__validators__': baseclass.__validators__}
    optional_fields = {key: (Optional[item.type_], None)
                       for key, item in fields.items()}
    return create_model(f'{baseclass.__name__}Optional', **optional_fields,
                        __validators__=validators)

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

ItemOptional = make_optional(Item)
