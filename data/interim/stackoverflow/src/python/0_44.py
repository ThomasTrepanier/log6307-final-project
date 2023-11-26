def solution(A,K):        
    for k in np.arange(K):
        B=[]
        for i in range(len(A)):
            B.append(A[i-1])
        A=B
    return B
