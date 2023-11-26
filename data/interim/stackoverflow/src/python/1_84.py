class User:
  def __init__(self, **data):
     self.__dict__ = data
  def __getattr__(self, _vals):
     yield from [getattr(self, i) for i in _vals.split('_')]

current_user = User(**currentUser)
id, email, gender, username = current_user.id_email_gender_username
id, gender = current_user.id_gender
