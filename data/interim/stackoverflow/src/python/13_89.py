class Example:

    def __init__(self, name):
        self.name = name

    def foo(self):
        self.name = 'John'

bar = Example('Jake')
bob = Example('Bob')
bar.foo()
print(bar.name)
print(bob.name)

John
Bob
