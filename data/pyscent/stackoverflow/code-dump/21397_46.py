def missing(arr1, arr2):
    #arr1 is the array of strings to be searched
    #arr2 is the array of substrings
    notFound=""
    for i in arr2: # i = each element in array 2
        for j in arr1: # j = each element in array 1
            if i in j: # if substring of i is in an element in j
                break # moves onto next element in the array
            elif j == arr1[-1]: # if not found in the string, checks if  on the last item in the array.
                notFound = notFound+" "+i
    if notFound != "":
        print("No key for value:", notFound)
    else:
        print("all elements of array2 exist in array1")
