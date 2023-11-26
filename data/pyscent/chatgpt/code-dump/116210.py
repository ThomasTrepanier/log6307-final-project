import math

def sigmodal(rank1, rank2, k=1):
    diff = abs(rank1 - rank2)
    if diff == 15:
        if rank1 < rank2:
            return 1, 0
        else:
            return 0, 1
    elif diff == 0:
        return 0.5, 0.5
    y = 1 / (1 + math.exp(-k * diff))
    if rank1 < rank2:
        return y, 1 - y
    else:
        return 1 - y, y
