def calculate_bill_amount2(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    for gem in gems_list:
        for g in reqd_gems:
            if g==gem:
                index = gems_list.index(g)
                no_of_gems = reqd_quantity[reqd_gems.index(g)]
                price = price_list[index] * no_of_gems
                print(price)
                bill_amount += price
            if g not in gems_list:
                return -1                
    return bill_amount
