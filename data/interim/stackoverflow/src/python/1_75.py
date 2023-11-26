from typing import List
from pydantic import BaseModel

class User(BaseModel):
  name: str
  age: int

class Users(BaseModel):
    users: List[User]

users = [{"name": "user1", "age": 15}, {"name": "user2", "age": 28}]
m = Users(users=users)
print(m.dict())
