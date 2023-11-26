from typing_extensions import Annotated

from pydantic import BaseModel, ConfigDict
from pydantic.functional_validators import AfterValidator

from bson.objectid import ObjectId


def object_id_validate(v: ObjectId | str) -> ObjectId | str:
    assert ObjectId.is_valid(v), f'{v} is not a valid ObjectId'
    if isinstance(v, str):
        return ObjectId(v)
    return str(v)


PyObjectId = Annotated[ObjectId | str, AfterValidator(object_id_validate)]


class MyModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    user_id: PyObjectId


print(MyModel(user_id=str(ObjectId()))) # user_id=ObjectId('653087c8c8640ef5700a1bb5')
print(MyModel(user_id=ObjectId())) # user_id='653087c8c8640ef5700a1bb6'
