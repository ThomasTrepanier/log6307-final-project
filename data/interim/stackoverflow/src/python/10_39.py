def mutator(state, comparator):
    while True:
        states = [0] + state + [0]
        state = [
            comparator(states[cellid-1], states[cellid+1])
            for cellid in range(1, len(states)-1)
        ]
        yield state

def cellCompete(states, days):
    generator = mutator(states, lambda x, y: x ^ y)

    for idx, states in enumerate(generator):
        if idx+2 > days:
            break

    return states

print(cellCompete([1,0,0,0,0,1,0,0] , 1))
print(cellCompete([1,1,1,0,1,1,1,1] , 2))
