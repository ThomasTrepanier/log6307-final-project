def circularArrayRotation(a, k, queries):
    #rotation
    for _ in range(k):
        a.insert(0, a.pop())
    #putting answer according to query
    ans = []
    for i in queries:
        ans.append(a[i])    
    return ans
