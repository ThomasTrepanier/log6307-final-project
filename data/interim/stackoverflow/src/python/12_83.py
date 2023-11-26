def first_and_last(message):
        if not message:
            return True
        if (message[0] == message[3]):
            return True
        elif (message[0] != message[3]):
            return False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
