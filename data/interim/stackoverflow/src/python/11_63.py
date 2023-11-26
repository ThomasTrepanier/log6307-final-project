def randDict(n):
    from random import randint

    keys  = ["key"+str(i) for i in range(n)]
    values = ["value"+str(i) for i in range(n)]
    final_dict={}
    for key in keys:
        final_dict[key]=values.pop(randint(0,n))

    return final_dict
