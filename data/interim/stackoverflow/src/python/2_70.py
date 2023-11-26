from timeit import repeat

book_ratings = []
for i in range(1000):
    book_ratings += [["Ben" + str(i)],["5", "0", "1", "4"]]    

def f1():
    i = iter(book_ratings)
    return dict((a[0], b) for a, b in zip(i, i))

def f2():
    return dict((a, b) for (a,), b in zip(book_ratings[::2], book_ratings[1::2]))

def f3():
    it = iter(book_ratings)
    return {k: next(it) for k, in it}

for _ in range(3):
    for f in f1, f2, f3:
        t = min(repeat(f, number=10000))
        print('%.2f' % t, f.__name__)
    print()
