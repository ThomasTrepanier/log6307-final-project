def most_frequent_letter(s):
    st = s.lower().replace(' ', '')
    frequencies = {}
    frequencies = {item: frequencies.setdefault(item, 0) + 1 for item in st}
    rev_freq = {count: key for key, count in frequencies.items()}
    return rev_freq[max(rev_freq)]

print(most_frequent_letter('nnmmmaaa'))  # -> a
