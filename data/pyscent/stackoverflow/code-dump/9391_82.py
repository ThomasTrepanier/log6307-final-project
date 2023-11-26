class User:
  def __init__(self, **data):
    self.__dict__ = data
  def __iter__(self):
    yield from [getattr(self, i) for i in ('id', 'email', 'gender', 'username')]

current_user = User(**currentUser)
id, email, gender, username = current_user
print([id, email, gender, username])
