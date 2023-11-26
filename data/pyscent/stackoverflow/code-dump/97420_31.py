def solution(data, n):
    from collections import OrderedDict
    dict1 = OrderedDict()

    for ele in data:
        dict1[ele] = dict1.get(ele,0)+1

    new_list = [k for k,v in dict1.items() if v<=n]
    return new_list
