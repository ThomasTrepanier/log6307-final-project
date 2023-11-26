import sys

term = sys.argv[1].strip().upper()
fruitlist = list(map(str.upper, sys.argv[2:]))


def search(term, lst):
    for item in lst:
        if item == term:
            return True


print(search(term, fruitlist))
