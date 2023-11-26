hour = float(input('Enter hours: '))
rate = float(input('Enter rates: '))

def compute_pay(hours, rates):

    if hours <= 40:
        pay = hours * rates
        return pay
    elif hours > 40:
        pay = ((hours * rate) - 40 * rate) * 1.5 + 40 * rate
        return pay

pay = compute_pay(hour, rate)
print(pay)
