import itertools 

def countways(l, target): 
    data = []  
    for length in range(1, target+1):  
        data.extend([x for x in itertools.combinations_with_replacement(l, length) if sum(x) == target]) 
    return len(data)
