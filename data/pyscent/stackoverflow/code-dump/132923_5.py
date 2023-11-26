def Solve(A):
    sumn = 0
    for i in range(len(A)):
        if A[i] in "aeiouAEIOU":
            sumn += len(A[i:])
    return sumn%10003
