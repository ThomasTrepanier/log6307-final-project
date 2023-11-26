ranges = [[0,5499],[5500,9499],[9500,14499],[14500,19499],[19500,24499],[24500,29499],[29500,34499],[34500,39499],[39500,44499]]
returns = [5000,10000,15000,20000,25000,30000,35000,40000,45000]

def checkRange(number):
    for i in range(len(returns)):
        if number in range(ranges[i][0], ranges[i][1]):
            return returns[i]

# Test a few values:
print(checkRange(10))
print(checkRange(6000))
