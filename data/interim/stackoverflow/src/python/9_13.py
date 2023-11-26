def LCM(minN,maxN):

    count = 1
    results = []
    for i in range(count,(maxN*count)+1):
        results.append(minN*count)
        count = count + 1
    print(results[-1]) # print the last elements of the list.
