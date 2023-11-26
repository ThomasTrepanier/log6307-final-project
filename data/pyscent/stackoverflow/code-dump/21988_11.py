def generate_all():
    some_list = [1,2,3]
    yield from generator(some_list)

for item in generate_all():
    ...
