import numpy as np
a = np.array([2,2,10,4,4,4,5,6,7,2,6,5,5,7,7,1,1])

def local_min(a):
    temp_list = list(a)
    maxval = max(a) #use max while finding minima
    temp_list = temp_list + [maxval] #handles last value edge case.

    prev = maxval #prev stores last value seen
    loc = 0 #used to store starting index of minima
    count = 0 #use to count repeated values
    #match_start = False
    matches = []
    for i in range(0, len(temp_list)): #need to check all values including the padded value
        if prev == temp_list[i]:
            if count > 0: #only increment for minima candidates
                count += 1
        elif prev > temp_list[i]:
            count = 1
            loc = i
    #        match_start = True
        else: #prev < temp_list[i]
            if count > 0:
                matches.append((loc, count))
            count = 0
            loc = i
        prev = temp_list[i]
    return matches

result = local_min(a)

for match in result:
    print ("{} minima found starting at location {} and ending at location {}".format(
            match[1], 
            match[0],
            match[0] + match[1] -1))
