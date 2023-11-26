def romanToInt(s):
    mapping  = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }
        
    min_ = None
    total = 0
    for c in s:
        val = mapping[c]
        print(val)
        if min_ and val > min_:
            total -= min_*2
        else:
            min_ = val
        total += val
                
    return total
