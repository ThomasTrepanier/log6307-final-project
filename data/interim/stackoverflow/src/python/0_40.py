def solution(A):
    A.sort()
    A.append(-1) #Just to make list even and run till last but not match with existing integers
    for i in range(0,len(A),2):
        if A[i]!=A[i+1]:
            return A[I]
