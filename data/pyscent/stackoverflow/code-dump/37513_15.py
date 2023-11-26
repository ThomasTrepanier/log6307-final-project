from collections import Counter

def keep_only_duplicated_items(lst):
    cnts = Counter(lst)
    for item in lst:
        if cnts[item] == 2:
            yield item
