def generator(some_list):
    for i in some_list:
        yield i

def generate_all():
    some_list = [1,2,3]
    yield 'start'
    yield from generator(some_list)
    yield 'end'

for item in generate_all():
    print(item)
