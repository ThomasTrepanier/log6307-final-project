list = { 'Name', 'Year', 'City_id', 'Region_Id' , 'Location', 'Source', 'Time'}

reqVal = { 'Name', 'Year', 'City_id' } # items in List - if present or not

def isValInList():
    assert True, reqVal.issubset(list)

isValInList()
