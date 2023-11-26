from itertools import groupby


def peaks(data):
    start = 0
    sequence = []
    for key, group in groupby(data):
        sequence.append((key, start))
        start += sum(1 for _ in group)

    for (b, bi), (m, mi), (a, ai) in zip(sequence, sequence[1:], sequence[2:]):
        if b < m and a < m:
            yield m, mi


print(list(peaks([0, 1, 2, 5, 1, 0])))
print(list(peaks([1, 2, 2, 2, 1])))
print(list(peaks([1, 2, 2, 2, 3])))
