from collections import OrderedDict
def get_unique_indexes(l):
    # OrdedDict is used to preserve the order of the indexes
    result = OrderedDict()
    for i in range(0, len(l)):
        val = l[i]
        if not val in result:
            result[val] = i

    return result.values()
