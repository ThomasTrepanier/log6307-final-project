data = [1, 0, 0, 0, 1, 1, 1, 0, 2, 3, 1, 0, 0, 1, 1, 1, 0]

def calc(data):
    sum = 0
    new = []
    for i in range(len(data)):
        if data[i] == 0:
            new.append(sum)
            if i == len(data) - 1:
                new.append(0)
            sum = 0
        else:
            sum = sum = sum + data[i]
            new.append(0)
            if i == len(data) - 1:
                new.append(sum)
    if new[0] == 0:
        del new[0]
    return new
