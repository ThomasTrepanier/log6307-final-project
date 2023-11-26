from functools import reduce

def getVowelsLength(word, k):
    chunks = [word[i:i+k] for i in range(len(word)-(k-1))]
    return reduce(lambda x, y: x if x[1] > y[1] else y, list(zip(chunks, [sum(1 for l in w if l in 'aeiou') for w in chunks])))
