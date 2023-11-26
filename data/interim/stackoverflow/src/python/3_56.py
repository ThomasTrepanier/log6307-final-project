def your_function(string): #Takes the combined string as input
    list1 = string.splitlines()
    list_to_return = []
    for x in list1:
        if list1.index(x) % 2 == 0:
            list_to_return.append(f'{x} \n {list1[list1.index(x) + 1]}')
    return list_to_return
