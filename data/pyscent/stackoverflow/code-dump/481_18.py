from bson import ObjectId
from pydantic import BaseModel


class ObjId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: str):
        try:
            return cls(v)
        except InvalidId:
            raise ValueError("Not a valid ObjectId")


class Foo(BaseModel):
    object_id_field: ObjId = None

    class Config:
        json_encoders = {
            ObjId: lambda v: str(v),
        }



obj = Foo(object_id_field="60cd778664dc9f75f4aadec8")
print(obj.dict())
# {'object_id_field': ObjectId('60cd778664dc9f75f4aadec8')}
print(obj.json())
# {'object_id_field': '60cd778664dc9f75f4aadec8'}
