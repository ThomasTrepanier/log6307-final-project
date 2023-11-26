@property
def some_prop(self):
    return "Family property"

@some_prop.setter
def some_prop(self, val):
    print(f"property setter is called!")
    # do something else...
