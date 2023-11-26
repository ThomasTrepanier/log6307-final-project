import random 

def calcVals(values, N):
    for i in range(N):
        values[i] = random.randint(1,6)

    # Remove brackets
    str_values = [str(i) for i in values] # convert to strings
    new_values = ", ".join(str_values)

    return values, str_values, new_values

N = 5 # number of dice throws
values = [0] * N

values, str_values, new_values = calcVals(values, N)
print("\nYou rerolled some dice and the new values are: {}".format(new_values))
