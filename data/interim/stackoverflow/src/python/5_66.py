def isValid(ip):
    ip = ip.split(".")

    for number in ip:
        if not number.isnumeric() or int(number) > 255:
            return False
    
    return True
