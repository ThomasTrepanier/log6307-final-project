def encode(message):
    result = []
    i = count = 0
    while i < len(message) - 1:
        count = 1
        while i + count < len(message) and message[i + count - 1] == message[i + count]:
            count += 1
        i += count
        result.append("{}{}".format(count, message[i - 1]))
    if count == 1:
        result.append("1" + message[-1])
    return result
