resultArray = [] #list

def hailstone(n):
    if n <= 0: # Base Condition
        return
    if n > 0:
       resultArray.append(n)
    if n > 1:
       if n % 2 == 0:
          hailstone(int(n/2))
       else:
          hailstone((n * 3) + 1)

# function call
hailstone(20)
print(len(resultArray), resultArray)
