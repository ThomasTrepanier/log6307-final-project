class Foo:
    def __new__(cls, a, b):
        print("Creating Instance")
        instance = super(Foo, cls).__new__(cls)
        return instance


    def __init__(self, a, b):
        self.a = a
        self.b = b

foo_1 = Foo(a=1, b=2)
foo_2 = Foo(a=1, b=3)
