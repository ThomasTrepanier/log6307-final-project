def get_sum_as_list(list1, list2):
    first_int = int(''.join(map(str,list1)))
    second_int = int(''.join(map(str,list2)))
    result = [int(num) for num in str(first_int+second_int)]
    return result
