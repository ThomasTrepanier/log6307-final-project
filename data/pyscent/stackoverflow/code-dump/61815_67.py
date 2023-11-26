from timeit import repeat

def summer_69_Accepted(lst):
    copyoflist = lst[:] # makes shallow copy of list
    while True:
        if 6 not in copyoflist:
            return sum(copyoflist)

        indexof6 = copyoflist.index(6)
        indexof9 = copyoflist.index(9, indexof6+1) # begin search for 9 after 6
        del copyoflist[indexof6:indexof9+1] 

def summer_69_Kelly1(lst):
    it = iter(lst)
    return sum(x for x in it
               if x != 6 or 9 not in it)

def summer_69_Kelly2(lst):
    it = iter(lst)
    total = 0
    for x in it:
        if x == 6:
            9 in it
        else:
            total += x
    return total

funcs = summer_69_Accepted, summer_69_Kelly1, summer_69_Kelly2

from random import randrange, choices

def testcase():
    def others():
        return choices([0, 1, 2, 3, 4, 5, 7, 8], k=randrange(10))
    lst = others()
    for _ in range(10):
        lst += [6, *others(), 9, *others()]
    return lst

tests = correct = 0
for _ in range(10):
    lst = testcase()
    expect = funcs[0](lst.copy())
    for func in funcs:
        result = func(lst.copy())
        correct += result == expect
        tests += 1
print(correct, 'out of', tests, 'tests correct')
print()

lst = [1] * 5000 + [6, 9] * 2500
for func in funcs:
    times = repeat(lambda: func(lst), number=1)
    print(*('%6d us ' % (t * 1e6) for t in sorted(times)), func.__name__)
