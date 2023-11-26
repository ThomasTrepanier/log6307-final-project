class FooSingleton:
    _instances = {}

    def __new__(cls, a, b):
        if cls not in cls._instances:
            print('creating new FooSingleton instance')
            cls._instances[cls] = super(FooSingleton, cls).__new__(cls)
        else:
            print('using FooSingleton instance')
        return cls._instances[cls]

    def __init__(self, a, b):
        self.a = a
        self.b = b

foo_s1 = FooSingleton(a=1, b=2)
foo_s2 = FooSingleton(a=1, b=3)
