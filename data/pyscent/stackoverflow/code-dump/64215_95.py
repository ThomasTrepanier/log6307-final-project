def split_check(bill, people, tax = 0.15, tip = 0.09):
    tax = bill * tax 
    tip = bill * tip
    return (bill + tax + tip)/people
    
print('Cost per diner:', split_check(25, 2))
