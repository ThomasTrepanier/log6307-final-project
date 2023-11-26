class Private:
    def __init__(self, attribute):
        self.attribute = attribute

    def __get__(self, obj, type=None):
        raise AttributeError("'{}' object has no attribute '{}'".format(obj, self.attribute))

    def __set__(self, obj, value):
        obj.__dict__[self.attribute] = value

class YourClass:
    private = Private('private')

    def __init__(self):
        self.private = 10
        print(self.private)  # Raise AttributeError
