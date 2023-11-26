# a strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down)
# find all strobogrammatic numbers that are of length = n
def findStrobogrammatic(self, n):
    nums = n % 2 * list('018') or ['']
    while n > 1:
        n -= 2
        # n < 2 is so genius here
        nums = [a + num + b for a, b in '00 11 88 69 96'.split()[n < 2:] for num in nums]
    return nums
