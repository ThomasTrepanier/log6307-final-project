def findIntersectionLofL(lofl):
    """Generalized findIntersection function which operates on a "list of lists." """
    K = len(lofl)
    indices = [0 for i in range(K)]
    result = []
    #
    try:
        while True:
            # idea is to maintain the indices via a construct like the following:
            allEqual = True
            for i in range(K):
                if lofl[i][indices[i]] < lofl[(i+1)%K][indices[(i+1)%K]] :
                    indices[i] += 1
                    allEqual = False
            # When the above iteration finishes, if all of the list
            # items indexed by the indices are equal, then another
            # item common to all of the lists must be added to the result.
            if allEqual :
                result.append(lofl[0][indices[0]])
                while lofl[0][indices[0]] == lofl[1][indices[1]]:
                    indices[0] += 1
    except IndexError as e:
        # Eventually, the foregoing iteration will advance one of the
        # indices past the end of one of the lists, and when that happens
        # an IndexError exception will be raised.  This means the algorithm
        # is finished.
        return result
