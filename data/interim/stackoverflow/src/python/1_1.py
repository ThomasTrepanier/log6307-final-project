def computeInt(nNum: int, nTimes: int) -> int:
    result = 0
    # how many times to multiple
    for i in range(0, nTimes):
        # result adding in each loop the iterator = 5 + n * str(5)
        # first is 5, second is 55, third is 555 the result is adding all of that as integer
        result += int(str(nNum) + i * str(nNum))
    return result


print(computeInt(5, 3))
