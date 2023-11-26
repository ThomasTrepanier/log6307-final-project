class Foo:
    def __init__(self, private):
        self.private = private

    def __getattribute__(self, attr):
        import inspect
        frame = inspect.currentframe()
        try:
            back_self = frame.f_back.__self__
            if not back_self == self: #is it inside the class?
                ban = ('private', '__dict__') #all private vars, ban __dict__ for no loopholes
                if attr in ban:
                    msg = 'Foo object has no attribute {!r}'
                    raise AttributeError(msg.format(attr))
        finally:
            del frame
        return super().__getattribute__(attr)

    def print_private(self):
        print(self.private) #access in the class!


foo = Foo('hi')
foo.print_private() #output: hi
foo.private #makes an error
