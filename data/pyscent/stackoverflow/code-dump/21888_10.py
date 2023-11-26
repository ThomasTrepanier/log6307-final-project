def generator(some_list):
    for i in some_list:
        raise Exception('exception happened :-)')
        yield i

def generate_all():
    some_list = [1,2,3]
    return generator(some_list)

for item in generate_all():
    ...
