def convert(A):
    B = [0] * len(A)
    partial_sum = 0
    for i in range(len(A) - 1):
        partial_sum += A[i]
        if A[i + 1] == 0:
            B[i] = partial_sum
            partial_sum = 0
            
    if A[-1] != 0:
        B[-1] = partial_sum + A[-1]
        
    return B
