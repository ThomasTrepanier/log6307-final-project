# https://stackoverflow.com/a/51915131/ @Divakar
def random_num_per_grp(L):
    # For each element in L pick a random number within range specified by it
    r1 = np.random.rand(np.sum(L)) + np.repeat(np.arange(len(L)),L)
    offset = np.r_[0,np.cumsum(L[:-1])]
    return r1.argsort()[offset] - offset

# a is input array
sidx = a.argsort()
c = np.bincount(a)
out = sidx[random_num_per_grp(c) + np.r_[0,c[:-1].cumsum()]]
