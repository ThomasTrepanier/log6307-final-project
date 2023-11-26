def RemoveDuplicate(numbers):

    result = []

    [result.append(e) for e in str(numbers) if not e in result]

    return int("".join(result))

data  = [[9112, 5625], [1232]]

for index, value in enumerate(data):
    for indexY, valueY in enumerate(value):
        data[index][indexY] = RemoveDuplicate(valueY)

print(data)
