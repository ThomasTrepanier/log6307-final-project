def isBalanced(s):
    opened = [0] # {}=3/-3, []=2/-2, ()=1/-1, others:0/-4
    for n in [3-("{[( )]}"+c).index(c) for c in s]:
        if not n&3 : continue
        elif n>0   : opened.append(n)
        elif opened.pop() != -n: return False
    return opened == [0]
