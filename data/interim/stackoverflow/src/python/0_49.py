from collections import deque
def solution(A, K):
    m=deque(A)
    m.rotate(K)
    return list(m)
