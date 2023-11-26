def most_frequent_letter(s):
    st = s.lower().replace(' ', '')
    st = st[::-1]
    frequencies = {}
    for items in st:
        if items in frequencies:
            frequencies[items] += 1
        else:
            frequencies[items] = 1

    return max(frequencies, key=frequencies.get)
