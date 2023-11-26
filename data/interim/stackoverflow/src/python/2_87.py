def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    j=0
    for i in reqd_gems:
        if i in gems_list:
            index=gems_list.index(i)
            bill_amount=bill_amount+reqd_quantity[j]*price_list[index]
            j=j+1
        else:
            bill_amount=-1
            break
    if(bill_amount>30000):
        bill_amount=bill_amount-(bill_amount*5/100)

    return bill_amount
