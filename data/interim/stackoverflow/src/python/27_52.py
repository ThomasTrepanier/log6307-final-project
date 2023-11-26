class ParentClass:

    def __init__(self, parent_arg):
        self.parent_arg = parent_arg


class ChildClass(ParentClass):

    def child_method(self):
        print(self.parent_arg)


c = ChildClass(parent_arg="Test")
c.child_method() # Output: Test
