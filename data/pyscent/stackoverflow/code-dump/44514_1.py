class human:
  def __init__(self, choice = False, **kwargs):
    self.details = [kwargs if choice is False else self._filterr(kwargs)][0]

  def _filterr(self, param):
    filtered = {k:v for k,v in param.items() if v is not None}
    return filtered

jason = human(choice = True ,name = "jason", age = None, height = None, gender = None, programmer = True)

print(jason.details)
