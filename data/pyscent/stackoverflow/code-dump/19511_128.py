import string
import timeit
import random
from collections import Counter

def f1(words):
    c = Counter()
    for word in words:
        c.update(set(word.lower()))
    return c

def f2(words):
    return Counter(
        c
        for word in words
        for c in set(word.lower()))

def f3(words):
    d = {}
    for word in words:
        for i in set(word.lower()):
            d[i] = d.get(i, 0) + 1
    return d


def f4(words):
    d = {c: len([w for w in words if c in w.lower()]) for c in string.ascii_lowercase} 
    return d


with open('words.txt') as word_file:
    valid_words = set(word_file.read().split())

for exp in range(5):

    result_list = []
    for i in range(1, 5):
        t = timeit.timeit(
            'f(words)',
            'from __main__ import f{} as f, valid_words, exp; import random; words = random.sample(valid_words, 10**exp)'.format(i),
            number=100)
        result_list.append((i, t))

    print('{:10,d} words | {}'.format(
        len(words),
        ' | '.join(
            'f{} {:8.4f} sec'.format(i, t) for i, t in result_list)))

print(f4(random.sample(valid_words, 10000)))
print(f4(random.sample(valid_words, 1000)))
print(f4(random.sample(valid_words, 100)))
print(f4(random.sample(valid_words, 10)))

