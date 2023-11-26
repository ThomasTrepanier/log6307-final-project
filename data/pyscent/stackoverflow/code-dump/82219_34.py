def valid(n):
    number = str(n)
    position = number.find("0")
    if "0" not in number:
        return 0
    return 1 + valid(number[(position+1):])
print("True" if valid(12340006)%2 ==0 else "False")
