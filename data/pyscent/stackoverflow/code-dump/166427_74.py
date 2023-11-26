a = [1,2,2,3,3,4,5,6]

from collections import defaultdict
def function(lis,n):
    dic = defaultdict(int)

    sol=set()

    for i in lis:
            try:
                if dic[i]:
                    pass
                else:
                    sol.add(i)
                    dic[i]=1
                    if len(sol)>=n:
                        break
            except KeyError:
                pass

    return list(sol)

print(function(a,3))
