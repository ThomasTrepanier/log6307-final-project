def flat(l):
    ret = list()
    for ll in l:
        if isinstance(ll, (OrderedDict, list)):
            ret.extend(flat(ll))
        else:
            ret.append(ll)
    return ret
