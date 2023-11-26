def get_names(list_of_interest):
    names = []
    for d in list_of_interest:
        if ininstance(d, list):
            names.extend(get_names(d))
        else:
            names.append(d['name'])
    return names 
