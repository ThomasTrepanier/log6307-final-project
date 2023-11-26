from itertools import groupby

def process_data(data):
    return [list(val for num in group) for val, group in groupby(data)]


def peaks(arr):
    #print(arr)
    posPeaks = {
    "pos": [],
    "peaks": [],
    }
    startFound = False
    n = 0
    while startFound == False:
        if arr[n][0] == arr[n+1][0]:
            n += 1
        else:
            startFound = True

    endFound = False
    m = len(arr) - 1
    while endFound == False:
        if arr[m][0] == arr[m-1][0]:
            m -= 1
        else:
            endFound = True

    for i in range(n+1, m):
        if arr[i][0] == arr[i-1][0]:
            None
        elif arr[i][0] >= arr[i-1][0] and arr[i][0] >= arr[i+1][0]:
            pos = sum([len(arr[idx]) for idx in range(i)])
            posPeaks["pos"].append(pos) #.append(i)
            posPeaks["peaks"].append(arr[i][0])
    return posPeaks



print(peaks(process_data([0, 1, 2, 5, 1, 0])))
print(peaks(process_data([1, 2, 2, 2, 1])))
print(peaks(process_data([1, 2, 2, 2, 3])))
