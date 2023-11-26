d = {
    "p_id": 1,
    "billing": {
        "first_name": "test"
    }
}


class Billing(BaseModel):
    first_name: str


class Data(BaseModel):
    p_id: int
    billing: Billing


class Order(MappingModel):
    p_id: int
    pre_name: str = Field(source='billing.first_name')


order = Order.build_from_model(Data(**d))
print(order.dict())
