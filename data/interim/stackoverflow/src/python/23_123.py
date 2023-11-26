def blackjack(a,b,c):  
    total = a+b+c
    if total <= 21:     
        return total
    elif 11 in [a,b,c] and total > 21:   
        new_total = total-10     
        if new_total > 21:    
            return 'Bust' 
        else:         
            return new_total   
    else: 
        return 'Bust'
