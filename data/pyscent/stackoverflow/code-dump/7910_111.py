def add_prefix(lst, prefix):
    return [prefix + str(x) for x in lst]

def create_sequences(lst, prefix='T'):
    groups = list(groupby_consecutive(lst))
    between = list(interperse(groups))

    result = add_prefix(groups[0], prefix)
    for x, y in zip(between, groups[1:]):
        result.extend(x + add_prefix(y, prefix))

    return result

sorted_ids = [1, 2, 4, 5, 8, 9, 10, 12, 13, 16, 17, 18, 20]
print(create_sequences(lst=sorted_ids))
# ['T1', 'T2', 'V', 'T4', 'T5', 'V', 'V', 'T8', 'T9', 'T10', 'V', 'T12', 'T13', 'V', 'V', 'T16', 'T17', 'T18', 'V', 'T20']
