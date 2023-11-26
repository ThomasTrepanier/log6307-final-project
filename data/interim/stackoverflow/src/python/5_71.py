def beginning(lst):
    ten=10
    a=0
    new_list=[]
    while a<len(lst) and lst[a]!='bye':
        new_list.append(lst[a])
        a+=1
    if len(new_list)>10 or len(new_list)==10:
        return new_list[:10]
    else:
        return new_list
