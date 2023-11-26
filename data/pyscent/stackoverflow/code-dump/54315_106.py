def is_power_of(number,base):
    if number == base:
        return True
    elif number < base:
        return False
    return is_power_of(number / base, base)
