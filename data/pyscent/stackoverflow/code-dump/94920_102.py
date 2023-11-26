class Specs():
    def __init__(self, a=None,b=None,c=None):
        self.a = a if a is not None else 'Apple'
        sefl.b = b if b is not None else 'Bravo'
        self.c = c if c is not None else 'Cherry'
example = Specs('Apple', None, 'Cherry')
