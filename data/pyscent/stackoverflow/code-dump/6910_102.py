def polyn(*roots):
    def _polyn(x):
        val = 1
        for r in roots:
            val *= x - r
        return val
    return _polyn

f3 = polyn(-2, 1, 2)

for i in range(-10, 11):
    assert f(i) == f3(i)
# Above code passed on Win 10, 3.7.2
