def circularArrayRotation(a, k, queries):
    reverse_a = list(reversed(a))
    reverse_a_copy = reverse_a.copy()
    for x in range(k):
        item = reverse_a[x]
        reverse_a_copy.remove(item)
        reverse_a_copy.append(item)
    line = []
    for x in queries:
        line.append(list(reversed(reverse_a_copy))[x])
    return line
