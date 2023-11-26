def primepartition(m):
    if m > 3:
        for number in range(m // 2, m - 1):
            difference = m - number

            for psuedoprime in range(2, int(number ** 0.5) + 1):
                if number % psuedoprime == 0 or difference > psuedoprime and difference % psuedoprime == 0:
                    break
            else:  # no break
                return number, difference  # as good a non-False result as any other...

    return False
