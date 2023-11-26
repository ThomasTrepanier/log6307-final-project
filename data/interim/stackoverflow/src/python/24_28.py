class Test:
    zeta = None
    def __init__(self):
        self.string = None

    def set_string(self, target_string):
        self.string = target_string
        print(self.string)
        Test.zeta = self.string

t = Test()
t.set_string('abc')
