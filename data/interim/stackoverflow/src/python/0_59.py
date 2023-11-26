def solution(A, K):
    for i in range(0, K): # will perform K iterations of the below code
        if A == []: # check if list is empty
            return A # return A if A is the empty list
        A.insert(0, A.pop()) # inserts at the first index of A the last element of A
    return A # will return the list A
