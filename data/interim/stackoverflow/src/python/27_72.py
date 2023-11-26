def gen_unique_zero_sum_list(num_members, min=-100, max=100):
    if int(num_members) < 1:
        raise ValueError
    ret = []
    # populate as many as we can randomly
    for i in range(0, int(num_members) - 2, 1):
        candidate = random.randint(min, max)
        while candidate in ret:
            candidate = random.randint(min, max)
        ret.append(candidate)
    if int(num_members) > 1:
        while len(ret) < int(num_members):
            # at this point we could get a forced duplicate
            candidate = random.randint(min, max)
            while candidate in ret:
                candidate = random.randint(min, max)
            final = -(sum(ret) + candidate)
            if final in ret or final == candidate:
                # we would have a duplicate, force two new numbers
                continue
            ret.append(candidate)
            ret.append(final)
    else:
        # this will always be zero, by definition
        ret.append(-sum(ret))
    return ret
