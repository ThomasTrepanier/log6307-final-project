def first_and_last(message):
    if not message:
        return True
    elif (message[0] == message[-1]):
        return True
    else:
        return False


print(first_and_last("else")) # Returns True
print(first_and_last("tree")) # Returns False
print(first_and_last("")) # Returns True
