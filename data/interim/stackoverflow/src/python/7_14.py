@property
def some_prop(self):
    return "Family property"

class Grandparent:
    culture = some_prop
    world_view = some_prop

class Parent(Grandparent):
    world_view = "Parent's new world_view"

class Child(Parent):
    def __init__(self):
        try:
            self.world_view = "Child's new world_view"
            self.culture = "Child's new culture"
        except AttributeError as exc:
            print(exc)
            self.__dict__['culture'] = "Child's desired new culture"
