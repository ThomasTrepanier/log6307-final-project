data = [100,50,3,205,10]

def findmax(data):
    a = data
    ma = a[0]
    mi = a[0]

    for item in data:
        if item > ma:
            ma = item

        if item < mi:
            mi = item

    return (ma,mi)

print(findmax(data))
