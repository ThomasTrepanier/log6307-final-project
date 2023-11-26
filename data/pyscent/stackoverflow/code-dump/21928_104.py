list = [ 'Name', 'Year', 'City_id', 'Region_Id' , 'Location', 'Source', 'Time']

reqVal = [ 'Name', 'Year', 'City_id', 'Test' ] # items in List - if present or not


def isValInList():
    foundCount = 0

    for val in reqVal:
        if val in list :
            print("Yes, '%s' required item is found in list" %  val)
            foundCount += 1

        else:
            print("No, '%s' required item is not in list" %  val)

    if foundCount == 0:
            print('No required items are found in list')



isValInList()

# output:
# Yes, 'Name' required item is found in list
# Yes, 'Year' required item is found in list
# Yes, 'City_id' required item is found in list
# No, 'Test' required item is not in list
