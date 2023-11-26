alist = ['Name', 'Year', 'City_id', 'Region_Id' , 'Location', 'Source', 'Time']

reqVal = ['Name', 'Year', 'City_id' ] # items in List - if present or not

def isValInList(alist, blist):
    global foundCount
    for num, entry_a in enumerate(alist):
        if entry_a in blist :
            print("Yes, %s required item is found in List : ", entry_a)
            foundCount += 1
        else:
            print('No required items are found in list')

isValInList(alist, reqVal)
