class User:
  def __init__ (self, **desc):
    self.desc = desc # whitelist items, if necessary

  def __str__ (self):
    [ name, age, gender ] = \
      destructure(self.desc, 'name', 'age', 'gender')

    return f"{name} ({gender}) is {age} years old"

# create users with keyword arguments
u = User(age = 2, gender = 'M')
v = User(gender = 'F', age = 3)
x = User(gender = 'F', name = 'Alice', age = 4)

print(u) # None (M) is 2 years old
print(v) # None (F) is 3 years old
print(x) # Alice (F) is 4 years old
