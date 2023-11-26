def my_gen(n: int):
    yield from range(n)

a = my_gen(10)
b = my_gen(8)
