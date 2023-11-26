def findListMatch(lists, match):
    # Loop over lists with indices
    for k, sublist in enumerate(lists):
        # Check if the beginning of the list matches the desired start pattern
        if sublist[0:len(match)] == match:
            # If it's a match, return the index
            return k
    # If none of the lists match, return a placeholder value of "None"
    return None

a = [['1','2','3','a','b'],
     ['4','5','6','c','d'],
     ['7','8','9','e','f']]

matchIndex = findListMatch(a, ['4', '5', '6'])

# Result:
# matchIndex = 1
