class MyClass:
    def __init__(self, a):
        self.a = a

    def add_one_to_a(self):
        self.a += 1


def test_method_add_one_to_a():
    initial_a = 1
    instance = MyClass(a=1)
    assert instance.a == initial_a  # we expect this to be 1
    instance.add_one_to_a()  # instance.a is now 2
    assert instance.a == initial_a + 1  # we expect this to be 2
