def add(a, b):
    return a + b

def test_add_function():
    a = 1
    b = 2
    assert add(a, b) == 3  # we KNOW that adding 1 + 2 must equal 3
