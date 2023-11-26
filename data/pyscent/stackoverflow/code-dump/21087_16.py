class Grandparent:
    @property
    def culture(self):
        return "Family property"
    
    # add a setter method
    @culture.setter
    def culture(self, val):
        print('Fine, have your own culture')
        # overwrite the child class attribute
        type(self).culture = None
        self.culture = val

class Parent(Grandparent):
    pass

class Child(Parent):
    def __init__(self):
        self.culture = "I'm a millennial!"

c = Child()
print(c.culture)
