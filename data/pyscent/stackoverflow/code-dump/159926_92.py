def circularArrayRotation(a, k, queries):

    new_arr = a[-k%len(a):] + a[:-k%len(a)]
    # list slicing is done here.  it will get the right rotated array 

    result = []
    for i in queries:
        result.append(new_arr[i])
        # running queries on rotated array
    return result
