def nth_common(lowered_words, check):
    m = []
    for i in lowered_words:
        m.append((i, lowered_words.count(i)))
    for i in set(m):
        # print(i)
        if i[1] == check: # check if the first index value (occurrance) of tuple == check
            print(i, "found")
    del m[:] # deleting list for using it again


words = ['apple', 'apple', 'apple', 'blue', 'BLue', 'call', 'cAlL']
lowered_words = [x.lower() for x in words]   # ignoring the uppercase
check = 2   # the check

nth_common(lowered_words, check)
