def __init__(self, child_arg, parent_arg):
    self.child_arg = child_arg
    super().__init__(parent_arg)

print(self.parent_arg) # This will then work
