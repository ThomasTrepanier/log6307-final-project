def solution(arr: list) -> int:
    '''
    for every char, check if still current sawtooth
    if still currently sawtooth, numberOfWays += length
    else reset temp counter
    '''
    l, r = 0, 1
    ways = 0
    while r < len(arr):

        # check if current char + past 2 chars are sawtooth
        if r-l > 1 and (arr[r-2] < arr[r-1] > arr[r] or
                        arr[r-2] > arr[r-1] < arr[r]):  
            ways += r-l

        # check if current char + past 1 chars are sawtooth
        elif arr[r-1] != arr[r]:                
            ways += 1
            l = r-1

        else:                                   
            # reset left pointer
            l = r

        r += 1
    return ways
