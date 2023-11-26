def enum_bins_dict(ints):
    enum_bins = defaultdict(list)
    for k, v in enumerate(ints):
        enum_bins[v].append(k)
    return enum_bins

def enum_bins_list(ints):
    enum_bins = [[] for i in range(ints.max() + 1)]
    for x, i in enumerate(ints):
        enum_bins[i].append(x)
    return enum_bins

def enum_bins_sparse(ints):
    M, N = ints.max() + 1, ints.size
    return sparse.csc_matrix((ints, ints, np.arange(N + 1)),
                             (M, N)).tolil().rows.tolist()
