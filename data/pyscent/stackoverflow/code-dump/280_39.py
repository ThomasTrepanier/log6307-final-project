from collections import Counter
def solution(A): 
    c = Counter(A)
    final = [k for k, v in c.items() if v == 1]
    return final[0]
