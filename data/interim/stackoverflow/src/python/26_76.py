import copy


def extract_one_list(xdata):
    """
    `xdata` .......... `external data`
    """
    old_type = type(xdata[0])
    # we are going to be testing for whether
    # two tuples have any elements in common.
    # For example, do (4, 5) and (7, 8) have any elements common?
    # the answer is `no`.
    prohibited_elements = set(xdata.pop(0))
    iout = [copy.copy(prohibited_elements)]
    # `iout`.......... `internal output`
    candi = 0
    while True:
        # `candi`......... candidate index
        # `candy`......... candidate
        if candi >= len(xdata):
            break
        candy = set(xdata[candi])
        if len(prohibited_elements.intersection(candy)) == 0:
            iout.append(candy)
            prohibited_elements.update(xdata.pop(candi))
        candi = candi + 1

    # Next, convert sets into the type of container
    # which was originally used (tuples, lists,
    # or some other type of container
    # Let external iout (xout) be:
    # the old_type of the internal element (ielem)
    # for each internal element in the internal iout (iout)
    xout = [old_type(ielem) for ielem in iout]
    return xout

def extract_all_lists(xdata):
    lol = list()
    # `lol`...... `list of lists`
    while len(xdata) > 0:
        lyst = extract_one_list(unsorted_data)
        lol.append(lyst)
    return lol

unsorted_data = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                 (1, 7), (1, 8), (1, 9), (1, 10), (2, 3),
                 (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
                 (2, 9), (2, 10), (3, 4), (3, 5), (3, 6),
                 (3, 7), (3, 8), (3, 9), (3, 10), (4, 5),
                 (4, 6), (4, 7), (4, 8), (4, 9), (4, 10),
                 (5, 6), (5, 7), (5, 8), (5, 9), (5, 10),
                 (6, 7), (6, 8), (6, 9), (6, 10), (7, 8),
                 (7, 9), (7, 10), (8, 9), (8, 10), (9, 10)]

lol = extract_all_lists(unsorted_data)
print('\n'.join([str(x) for x in lol]))
