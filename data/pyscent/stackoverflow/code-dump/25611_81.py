from operator import itemgetter

allBins = [[(3,20)],[(1,11),(0,6)],[(4,16),(2,5)]]

def func(bin_num, all_bins):
    bin = itemgetter(bin_num)(all_bins)
    s = sum(map(itemgetter(-1), bin))
    return s

print(func(2, allBins))
# 21
