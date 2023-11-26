def name_lists(name_list):
    d = {}
    
    for name in name_list:
                
        first_name = name.split()[0]
        if first_name in d:
            
            d[first_name].append(name)
            d[first_name].sort()
            
        else:
            d[first_name]=[name]

    return d
