def end_zeros(a: int) -> int:  
    count = 0 
    list = [int(x) for x in str(a)]
    list.reverse()
    list.append(1)
    for x in list:
        if x == 0:
            count += 1            
        else:
            return count
