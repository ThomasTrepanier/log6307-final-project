def find_index(s, n):
    length = len(s.split()[n])
    index = [(0, len(s.split()[0]) - 1)]
    for i in s.split():
        index.append((index[-1][0] + len(i), index[-1][1] + len(i)))
    return index[n + 1]
print(find_index('cold weather gives me cold', 4))
