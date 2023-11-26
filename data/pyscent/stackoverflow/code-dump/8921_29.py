from math import comb
def solution(arr):
    
    n=len(arr)
    
    if arr[1]!=arr[0]:
        l=2
        
    else:
        l=0
    pre=arr[1]-arr[0]
    ans=0
    
    for i in range(2,n):
        cur=arr[i]-arr[i-1]
        
        if cur*pre<0:
            l+=1
        else:
            if l==2:
                ans+=1
            elif l==0:
                ans+=0
            else:
                ans+=comb(l,2)
            if cur!=0:
                l=2
            else:
                l=0
        pre=cur
    if l==2:
        ans+=1
    elif l==0:
        ans+=0
    else:
        ans+=comb(l,2)
    return ans
