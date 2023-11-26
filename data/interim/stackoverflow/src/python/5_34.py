from timeit import timeit


first = """
def get_from_two_sets():
    seen = set()
    ans = set()

    for el in (2, 3, 6, 6, 8, 9, 12, 12, 14):
        if el not in seen:
            seen.add(el)
            ans.add(el)
        else:
            ans.discard(el)"""


second = """

def get_from_counter():
    return [el for el, cnt in Counter((2, 3, 6, 6, 8, 9, 12, 12, 14)).items() if cnt == 1]
    """


print(timeit(stmt=first, number=10000000))
print(timeit(stmt=second, number=10000000, setup="from collections import Counter"))
