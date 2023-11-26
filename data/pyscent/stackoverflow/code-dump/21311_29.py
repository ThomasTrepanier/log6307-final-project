def GetNumbersInBetween(lst, l_Bound, u_Bound):
    n_List = []

    lowerBound = min(l_Bound, u_Bound)   # Get the lower val
    upperBound = max(l_Bound, u_Bound)   # Get the higher val

    for x in lst:
        if x >= lowerBound and x <= upperBound:
            n_List.append(x)
    return n_List

lst = [9, 10, 11, 15, 19, 20, 21]

lowerBound = 20       # intentionally given the wrong value
upperBound = 10       # intentionally given the wrong value

print(GetNumbersInBetween(lst, lowerBound, upperBound))
