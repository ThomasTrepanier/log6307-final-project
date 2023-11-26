def except_zero(items: list) -> Iterable: 
    ans=[]
    ind=[]
    for i in range(len(items)): 
        if (items[i] != 0): 
            ans.append(items[i]) 
            ind.append(i)

    ans = list(sorted(ans))
    for i in range(len(ind)): 
            items[ind[i]] = ans[i] 
    return items
