import collections.abc 

def isCorrectType(data):
    if isinstance(data, collections.abc.Collection): 
        for d in data:
            if isinstance(d,collections.abc.MutableMapping): 
                for key in d:
                    if isinstance(key,str) and isinstance(d[key],int):
                        pass
                    else:
                        return False
            else: 
                return False
    else:
        return False
    return True
