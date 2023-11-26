rangeList =  [5499, 9499, 14499, 19499, 24499, 29499, 34499, 39499, 44499]
returnList = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000]

def checkRange(number):
    for i in range(len(rangeList)):
        if number<=rangeList[i]:
            return returnList[i]
    return -1

inp: checkRange(5499)
op: 5000
