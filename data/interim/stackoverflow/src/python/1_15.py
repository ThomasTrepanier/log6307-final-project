import enum
from pydantic import BaseModel


class Group(enum.Enum):
    user = 0
    manager = 1
    admin = 2


class User(BaseModel):
    id: int
    username: str
    group: Group

    class Config:
        json_encoders = {Group: lambda g: g.name}


user = User(id=5, username="admin", group=2)
print(user)  # id=5 username='admin' group=<Group.admin: 2>
print(user.json())  # {"id": 5, "username": "admin", "group": "admin"}
