def stop_at_four():
    list_=[3,6,4,1,3]
    accum_lst=[]
    accum_var=0

    while list_[accum_var] != 4 :
        accum_lst.append(list_[accum_var])
        accum_var += 1
    return accum_lst

print(stop_at_four())
