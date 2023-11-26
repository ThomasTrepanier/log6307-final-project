from itertools import count

def gen(value):
    """Returns a generator that first yields `value` and then `value + x * 0.10` (where x is 1, 2, ...).
    """
    yield value
    yield from map(lambda x: value + x * 0.10, count(1))

my_list = [20, 20, 20, 30, 20, 30, 40, 50, 15, 11, 20, 40, 50, 15]

# create a generator for each distinct value in my_list
generators = {k: gen(k) for k in set(my_list)}

# calculate the result list
dup_list = [next(generators[elmt]) for elmt in sorted(my_list)]

print(dup_list)
