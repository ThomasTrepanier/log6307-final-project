def sum_of_even(upperlim, lowerlim = 2):
    if upperlim <= lowerlim:
        if upperlim == lowerlim:
            return upperlim
        else:
            return 0
    midpoint = lowerlim + (upperlim - lowerlim) // 2
    if midpoint % 2 == 0:
        return sum_of_even(upperlim, midpoint + 2) + sum_of_even(midpoint, lowerlim)
    else:
        return sum_of_even(upperlim, midpoint + 1) + sum_of_even(midpoint - 1, lowerlim)

def cross_check(n):
    half_n = n // 2
    return half_n * (half_n + 1)

n = 1000000
print(sum_of_even(n))   # => 250000500000
print(cross_check(n))   # => 250000500000
