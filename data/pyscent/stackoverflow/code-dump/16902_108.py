def calculate_bill_amount(gem_prices, reqd_gem_quantities):
    bill_amount = 0
    for gem in reqd_gem_quantities: 
        if gem in gem_prices:
            price = gem_prices[gem] * reqd_gem_quantities[gem]
            bill_amount += price
        else:
            return -1
    return bill_amount

gem_prices = { "Emerald": 1760, "Ivory": 2119, "Jasper": 1599, "Ruby": 3920, "Garnet": 3999 }
reqd_gem_quantities = { "Ivory": 3, "Emerald": 2, "Garnet": 5 }

print(calculate_bill_amount(gem_prices, reqd_gem_quantities))
