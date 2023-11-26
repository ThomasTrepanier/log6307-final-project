from collections import defaultdict, Counter
import timeit

orders = ["screws:20", "nails:15", "brushes:5", "screws:15", "nails:20"]

def solution_wjandrea():
    tally = Counter()
    for s in orders:
        item, count = s.split(":")
        tally[item] += int(count)
    return tally

def solution_jan():
    dct = defaultdict(int)

    for item in orders:
        key, value = item.split(":")
        dct[key] += int(value)
    return dct

print(timeit.timeit(solution_wjandrea, number=10**6))
print(timeit.timeit(solution_jan, number=10**6))
