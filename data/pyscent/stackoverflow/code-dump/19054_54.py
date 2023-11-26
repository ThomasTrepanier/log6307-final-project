from pydantic import BaseModel

d = {
    "p_id": 1,
    "billing": {
        "first_name": "test"
    }
}


class Order(BaseModel):
    p_id: int
    pre_name: str

    def __init__(self, **kwargs):
        kwargs["pre_name"] = kwargs["billing"]["first_name"]
        super().__init__(**kwargs)


print(Order.parse_obj(d))  # p_id=1 pre_name='test'
