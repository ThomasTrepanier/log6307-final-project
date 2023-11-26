s = "aaabbbd"
def check_freq(s):
    freq = {}
    for c in s:
        freq[c] = s.count(c)
    for w in sorted(freq, key=freq.get, reverse=True):
        if freq[w] == 1 or freq[w] == 2:
            del freq[w]
        else:
            print (w, freq[w])
print(freq)

check_freq(s)
