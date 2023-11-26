L = [1,2,3,4,5,6,7,8,9]

def takeuntil(lst, max_value = 0):
    """Yields elements as long as the cummulative sum is smaller than max_value."""
    total = 0
    for item in lst:
        total += item
        if total <= max_value:
            yield item
        else:
            raise StopIteration

    raise StopIteration

new_lst = [item for item in takeuntil(L, 20)]
print(new_lst)
