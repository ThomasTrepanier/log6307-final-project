class Bar:
    @si.inject('foo')
    def my_method(self, a, b, foo, kwarg1=30):
        return foo(a, b, kwarg1)

print(Bar().my_method(1, 2, kwarg1=50)) # = 53
