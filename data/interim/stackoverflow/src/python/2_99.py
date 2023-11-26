cache = {}
def collatz(n):
    sequenceLength = 0
    while (n>=1):
        if n in cache:  # number already encountered
            return sequenceLength + cache[n]
        if (n==1):
            break # solution is found
        elif (n%2==0):
            n = n/2
            sequenceLength += 1
        else:
            n = 3*n+1
            sequenceLength += 1
    return sequenceLength

def longest_seq(limit):
    result = []
    for i in range(1, limit+1):
        c = collatz(i)
        result.append(c)
        cache[i] = c  # put the answer in the cache

    print(result)
    return max(result)
