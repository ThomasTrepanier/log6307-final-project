def solution(A):
    cloned = []
    A.sort()
    if len(A) > 1:
       for itr in A:
          if itr in cloned:
             itrindex = cloned.index(itr)
             cloned.pop(itrindex)
          else:
             cloned.append(itr)
    else:
        return A[0]

    return cloned[0]
