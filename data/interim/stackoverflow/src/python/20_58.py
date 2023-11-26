    # MaxCounters
def solution(N, A):
    max_counter = 0
    list_counters = [0]*N
    if N < min(A):
        return list_counters
    for i in A:
        if i <= N:
            list_counters[i-1] += 1
            max_counter = max(list_counters[i-1], max_counter)
        else:
            list_counters = [max_counter]*N
    return list_counters
