def gen_unique_zero_sum_list(num_members):
    ret = []
    for i in range(int(num_members) - 1):
        candidate = random.randint(-100, 100)
        while candidate in ret:
            candidate = random.randint(-100, 100)
        ret.append(candidate)
    ret.append(-sum(ret))
    return ret
