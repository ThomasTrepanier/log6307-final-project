def another_foo(self):
  self.name = 'Mark'
baz = Example('Jake')
another_foo(baz)
print(baz.name)  # Mark
