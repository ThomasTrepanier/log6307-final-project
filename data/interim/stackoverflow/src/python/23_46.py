import itertools

def zip_first(lists):
    equal_lists = [l[:len(lists[0])] for l in lists]
    return itertools.zip_longest(*equal_lists)
