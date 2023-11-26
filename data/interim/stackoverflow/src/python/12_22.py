from dataclasses import dataclass
from dacite import from_dict


@dataclass
class User:
    name: str
    age: int
    is_active: bool


data = {
    'name': 'John',
    'age': 30,
    'is_active': True,
    "extra_1": 1000,
    "extra_2": "some value"
}

user = from_dict(data_class=User, data=data)
print(user)
# prints the following: User(name='John', age=30, is_active=True)
