def solution(N, A):
    counters = [0] * N
    max_c = 0
    last_was_max = False
    for el in A:
        if el <= N:
            counters[el - 1] += 1
            max_c = max(counters[el - 1], max_c)
            last_was_max = False
        elif not last_was_max:
            counters = [max_c] * N
            last_was_max = True
    return counters


def solution2_1(N, A):
    counters = [0] * N
    last_was_max = False
    for el in A:
        if el <= N:
            counters[el - 1] += 1
            last_was_max = False
        elif not last_was_max:
            counters = [max(counters)] * N
            last_was_max = True
    return counters
