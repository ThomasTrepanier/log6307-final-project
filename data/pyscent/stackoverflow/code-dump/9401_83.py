class User:
  def __init__(self, **data):
    self.__dict__ = data
  def __iter__(self):
    for i in ('id', 'email', 'gender', 'username'):
      yield getattr(self, i)
