def solution(N, A):
    # write your code in Python 3.6
    maxcount=0
    counter=[maxcount]*N
    can_be_updated = True
    for J in A:
        if(J<=N ):
            counter[J-1]+=1
            maxcount = max(maxcount,counter[J-1])
            can_be_updated = True
        else:
            if(can_be_updated):
                counter = [maxcount]*N
                can_be_updated = False
    return(counter)   
pass
