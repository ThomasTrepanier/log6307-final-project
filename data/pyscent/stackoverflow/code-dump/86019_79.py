import collections
def repfree(s):
    results = collections.Counter(s)
    for i in results:
        if results[i] > 1:
            return False
    return True
