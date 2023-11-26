import collections

def generators_factory(iterable):
    it = iter(iterable)
    deques = []
    already_gone = []

    def new_generator():
        new_deque = collections.deque()
        new_deque.extend(already_gone)
        deques.append(new_deque)

        def gen(mydeque):
            while True:
                if not mydeque:             # when the local deque is empty
                    newval = next(it)       # fetch a new value and
                    already_gone.append(newval)
                    for d in deques:        # load it to all the deques
                        d.append(newval)
                yield mydeque.popleft()

        return gen(new_deque)

    return new_generator

# test it:
infinite_stream = [1, 2, 3, 4, 5]
factory = generators_factory(infinite_stream)
gen1 = factory()
gen2 = factory()
print(next(gen1)) # 1
print(next(gen2)) # 1 even after it was produced by gen1
print(list(gen1)) # [2, 3, 4, 5] # the rest after 1
