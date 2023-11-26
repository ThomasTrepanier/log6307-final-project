class A:

    def __init__(self, field):
        self.methods = [self.method]
        self.field = field

    def __eq__(self, other):
        import deepdiff
        if type(self) != type(other):
            return False
        return deepdiff.DeepDiff(self.__dict__, other.__dict__) == {}

    def method(self):
        pass
