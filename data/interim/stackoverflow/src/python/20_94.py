def solution2(N, A):
    counters = [0] * N
    for el in A:
        if el <= N:
            counters[el - 1] += 1
        else:
            counters = [max(counters)] * N
    return counters
