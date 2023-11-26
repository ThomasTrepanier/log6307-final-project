@si.register(name='uppercase')
class UpperCaseRepresentation:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value.upper()
