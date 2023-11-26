def contains(sub_array, array):
    for i in range(len(array)-len(sub_array)+1):
        for j in range(len(sub_array)):
            if array[i+j] != sub_array[j]:
                break
        else:
            return i, i+len(sub_array)
    return False
