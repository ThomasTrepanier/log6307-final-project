def stop_at_four(lis):
    new_list = []
    start = 0
    while start < len(lis) and lis[start] != 4:
        new_list.append(lis[start])
        start += 1
    return new_list    
    
list1 = [1, 6, 2, 3, 9]     
print(stop_at_four(list1))
