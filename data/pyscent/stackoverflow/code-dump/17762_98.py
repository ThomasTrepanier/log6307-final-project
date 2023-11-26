cache = {1:0}
def collatz(n):
    if n in cache:
       return cache[n]
    else:
       if n%2==0:
          m = n//2
       else:
          m = 3*n+1
       res = collatz(m) + 1
       cache[n] = res
       return res


def longest_seq(limit):
    result = []
    for i in range(1, limit+1):
        result += [collatz(i)]
    return max(result)
