import math
def narcissistic(value):
    n = math.floor(math.log10(value)) + 1
    x = [math.floor((value/10**i)%10)**n for i in range(n)]   
    print(sum(x) == value)

narcissistic(371)
#True
