import random as r

def spreadRandom(theRange, howMany, minSpacing):
    while True:
        candidate = sorted([r.randint(*theRange) for _ in range(howMany)])
        minDiff = min([ candidate[i+1]-candidate[i] for i, _ in enumerate(candidate[:-1])])
        if minDiff >= minSpacing:
            return candidate

spreadRandom([0,200], 5, 15)
