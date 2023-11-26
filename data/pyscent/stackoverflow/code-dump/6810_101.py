def poly3(r1, r2, r3):
    def _poly3(x):
        return (x - r1) * (x - r2) * (x - r3)
    return _poly3

f2 = poly3(-2, 1, 2)

for i in range(-10, 11):
    assert f(i) == f2(i)
# no AssertionError means all tests pass
