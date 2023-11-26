def arrange_tickets(tickets_list):
    ids = [int(ticket[1:]) for ticket in tickets_list]
    expected_ids = range(1, max(ids) + 1)
    listt=["T%d" % n if n in ids else "V" for n in expected_ids]
    list1=listt[0:10]
    list2=listt[11:]
    for i in range(10):
        if 'V' in list2:
            list2.remove('V')
    for j in range(0,len(list2)):
        for n, i in enumerate(list1):
            if i == 'V':
                list1[n] = list2[j]
                j+=1
    return list1
tickets_list = ['T5','T7','T1','T2','T8','T15','T17','T19','T6','T12','T13']
print("Ticket ids of all the available students :")
print(tickets_list)
result=arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result[0:10])
