def slice(A):
    B = []
    for i  in range(0,len(A)) :
        B.append(A[-1+i])
    return B 

def solution(A, K):
    for i in range (1,K+1):
        A = slice(A)
    return A
