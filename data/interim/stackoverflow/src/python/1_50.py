from models.PyObjectId import PyObjectId
from pydantic import BaseModel, Field as PydanticField
from bson import ObjectId
class Users(BaseModel):
    id: PyObjectId = PydanticField(default_factory=PyObjectId, alias="_id")
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True #required for the _id 
        json_encoders = {ObjectId: str}
