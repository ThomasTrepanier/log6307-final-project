class ChildClass(ParentClass):

    def __init__(self, child_arg):
        self.child_arg = child_arg

    def child_method(self):
        print(self.child_arg) # Output: Child Test

        # This will throw an error since this attribute is created by the parent constructor
        print(self.parent_arg)

c = ChildClass(child_arg="Child Test")
c.child_method()
