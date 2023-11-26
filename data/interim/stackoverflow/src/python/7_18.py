class Grandparent:
    # ...
    def overwrite_props(self):
        # reassign class attributes
        type(self).size = None
        type(self).len = None
        # other properties, if necessary

# ...

# Usage
class Child(Parent):
    def __init__(self):
        self.overwrite_props()
        self.size = 5
        self.len = 10
