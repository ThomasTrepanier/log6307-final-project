def unordered_eq(A, B):
    for a in A:
        if A.count(a) != B.count(a):
            return False
    return True
