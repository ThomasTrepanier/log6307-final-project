def findIntersectionLofLunRolled(lofl):
    """Generalized findIntersection function which operates on a "list of lists."
Accepts a list-of-lists, lofl.  Each of the lists must be ordered.
Returns the list of each element which appears in all of the lists at least once.
"""
    K = len(lofl)
    indices = [0] * K
    result = []
    lt = [ (i, (i+1) % K) for i in range(K) ] # avoids evaluation of index exprs inside the loop
    #
    try:
        while True:
            allUnEqual = True
            while allUnEqual:
                allUnEqual = False
                for i,j in lt:
                    if lofl[i][indices[i]] < lofl[j][indices[j]]:
                        indices[i] += 1
                        allUnEqual = True
            # Now all of the lofl[i][indices[i]], for all i, are the same value.
            # Store that value in the result, and then advance all of the indices
            # past that common value:
            v = lofl[0][indices[0]]
            result.append(v)
            for i,j in lt:
                while lofl[i][indices[i]] == v:
                    indices[i] += 1
    except IndexError as e:
        # Eventually, the foregoing iteration will advance one of the
        # indices past the end of one of the lists, and when that happens
        # an IndexError exception will be raised.  This means the algorithm
        # is finished.
        return result
