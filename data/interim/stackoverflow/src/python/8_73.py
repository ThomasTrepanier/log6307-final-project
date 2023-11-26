def max_unique_substrings(s, seen=()):
    maximum = 0
    for i in range(1, len(s) + 1):
        candidate = s[:i]
        if candidate not in seen:
            maximum = max(maximum, 1 + max_unique_substrings(s[i:], {candidate, *seen}))
    return maximum
