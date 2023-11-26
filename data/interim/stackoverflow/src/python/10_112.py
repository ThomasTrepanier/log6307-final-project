def arrange_tickets(tickets_list):
    ids = [int(ticket[1:]) for ticket in tickets_list]
    expected_ids = range(1, max(ids) + 1)
    return ["T%d" % n if n in ids else "V" for n in expected_ids]

tickets_list = ['T20', 'T5', 'T10', 'T1', 'T2', 'T8', 'T16', 'T17', 'T9', 'T4', 'T12', 'T13', 'T18']
print("Ticket ids of all the available students :")
print(tickets_list)
result=arrange_tickets(tickets_list)
print(result)   
