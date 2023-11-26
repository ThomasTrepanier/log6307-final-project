def blackjack(x,y,z):
    tot=int(x+y+z)
    if tot < 21:
        return tot
    
    elif tot > 21 and x == 11 or y == 11 or z == 11:
        tot2=tot-10
        return tot2
    
    else:
        return "BUST"
        
    
    
print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))
