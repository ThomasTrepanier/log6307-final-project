def stop_at_four(my_list):
    accum_lst=[]
    accum_var=0

    while (accum_var < len(my_list)) and (my_list[accum_var] != 4):
        accum_lst.append(my_list[accum_var])
        accum_var+=1
    return accum_lst

print(stop_at_four([3,6,4,1,3]))
