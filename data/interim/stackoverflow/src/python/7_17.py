class Grandparent:
    # ...
    @culture.setter
    def culture(self, val):
        if isinstance(val, tuple):
            if val[1]:
                print('Fine, have your own culture')
                type(self).culture = None
                self.culture = val[0]
        else:
            raise AttributeError("Oh no you don't")

# ...

class Child(Parent):
    def __init__(self):
        try:
            # Usual setter
            self.culture = "I'm a Gen X!"
        except AttributeError:
            # Trigger the overwrite condition
            self.culture = "I'm a Boomer!", True
