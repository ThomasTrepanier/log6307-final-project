def solution(A): 
     
    num = 0

    for i in range(len(A)): 
        num = num ^ A[i]        
         
    return num
