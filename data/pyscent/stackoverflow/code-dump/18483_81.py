def hillValey(A):
    if len(A)<3: return
    p1,p2,p3 = A[:3]
    for p in A[3:]:
        if p==p3 : continue
        if  p1==p2 or (p1>p2) == (p2>p3):
            p1,p2,p3 = p2,p3,p
        elif (p3>p) == (p2>p3) :
            p3=p
        else: return
    if p1==p2 or p2==p3:   return
    if (p1<p2) != (p2>p3): return
    return "Valley" if p1>p2 else "Hill"
