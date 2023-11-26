import timeit, os

def sort_u10(l):
    l[1:] = sorted(l[1:])

def sort_chris(l):
    l = l[:1] + sorted(l[1:])

def sort_heap(l, smallest=float('-inf')):
    tmp = l[0]
    l[0] = smallest
    l.sort()
    l[0] = tmp

def sort_heap2(l):
    tmp = l[0]
    l[0] = -1
    l.sort()
    l[0] = tmp

for _ in range(3):
    for sort in sort_u10, sort_chris, sort_heap, sort_heap2, sort_rev:
        number, repeat = 1_000_000, 5
        data = iter([[2, 4, 1, 3, 5] for _ in range(number * repeat)])
        # number, repeat = 50_000, 5
        # data = iter([[int(x) for x in os.urandom(100)] for _ in range(number * repeat)])
        t = timeit.repeat(lambda: sort(next(data)), number=number, repeat=repeat)
        print('%10s %.4f seconds' % (sort.__name__, min(t)))
    print()
