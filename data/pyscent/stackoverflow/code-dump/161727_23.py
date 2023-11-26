def ways(l, target):
    dp =[ [] for i in range(target+1) ]
    l.sort()
    n=len(l)
    for i in range(n):
        for j in range(l[i], target+1):    
            if j==l[i]:
                dp[j].append([l[i]])
            else:
                if dp[j-l[i]]:   
                    for u in dp[j-l[i]]:       
                        dp[j].append(u+[l[i]])       
    return dp[-1]

if __name__ == "__main__":
     l = [1,2,3] 
     target = 5
     print(len(ways(l, target)))
     l = [5, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
     target = 30
     print(len(ways(l, target)))
