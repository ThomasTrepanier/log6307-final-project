from dataclasses import astuple, dataclass

@dataclass
class User:
    id: int
    name: str
    website: str
    description: str
    email: str
    gender: str
    phone_number: str
    username: str
    
    def __iter__(self):
        return iter(astuple(self))
    
    def __getitem__(self, keys):
        return iter(getattr(self, k) for k in keys)
        

current_user = User(id=24, name="Jon Doe", website="http://mywebsite.com", description="I am an actor", email="example@example.com", gender="M", phone_number="+12345678", username="johndoe")

# Access fields sequentially:
id, _, email, *_ = current_user
# Access fields out of order:
id, email, gender, username = current_user["id", "email", "gender", "username"]
