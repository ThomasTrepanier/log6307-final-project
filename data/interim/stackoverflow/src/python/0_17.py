from pydantic import BaseModel, create_model

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

UpdateItem = create_model(
    'UpdateItem',
    __base__=Item,
    **{k: (v.annotation, None) for k, v in Item.model_fields.items()}
)
