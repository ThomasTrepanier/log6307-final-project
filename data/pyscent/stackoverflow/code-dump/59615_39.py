def split_check(bill=0, people=0, tax_percentage=0.09, tip_percentage=0.15):
    new_check = (bill * tax_percentage) + bill
    new_tip = bill * tip_percentage
    per_person = (new_check + new_tip) / people
    return per_person

bill = float(input())
people = int(input())

# Cost per diner at the default tax and tip percentages
print('Cost per diner:', split_check(bill, people))

bill = float(input())
people = int(input())
new_tax_percentage = float(input())
new_tip_percentage = float(input())

# Cost per diner at different tax and tip percentages
print('Cost per diner:', split_check(bill, people, new_tax_percentage, new_tip_percentage))
