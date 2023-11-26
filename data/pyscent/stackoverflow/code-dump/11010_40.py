def process(state, r):
    n = int(''.join(map(str,state)), 2)
    for i in range(r):
        n = ((n ^ n << 2) >> 1) % 256

    return list(map(int,format(n, "08b")))

process([1,1,1,0,1,1,1,1], 2)
# [0, 0, 0, 0, 0, 1, 1, 0]

process([1,0,0,0,0,1,0,0] , 1)
# [0, 1, 0, 0, 1, 0, 1, 0]
