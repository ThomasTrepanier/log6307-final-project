import itertools

def my_gen(n:int):
    for i in range(n):
        yield i

gen1 = my_gen(10)
gen2 = my_gen(8)

for i, j in itertools.zip_longest(gen1, gen2):
    print(i, j)
