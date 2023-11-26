def H_with_list(n, list_final):
    if n == 1:
        list_final.append(1)
        return list_final
    else:
        list_temp = H_with_list(n-1, list_final)
        list_final.append(2*list_temp[-1]+1)
        return list_final
