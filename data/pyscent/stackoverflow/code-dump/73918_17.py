from pydantic.dataclasses import dataclass
from pydantic.tools import parse_obj_as
import dataclasses
import json

@dataclass
class User:
  id: int
  name: str

user = User(id=123, name="James")
user_json = json.dumps(dataclasses.asdict(user))
print(user_json)  # '{"id": 123, "name": "James"}'

user_dict = json.loads(user_json)
user = parse_obj_as(User, user_dict)
print(user)  # User(id=123, name='James')
