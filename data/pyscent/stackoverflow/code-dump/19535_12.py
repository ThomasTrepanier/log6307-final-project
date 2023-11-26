def beginning(lst):
    new_list = []
    start = 0
    while start < 10 and lst[start] != 'bye':
        new_list.append(lst[start])
        start += 1
        
    return new_list

list1 = ["Hello", "There", "bye", "Hi", "K", "EHEH", "Edkf"]
print(beginning(list1))
