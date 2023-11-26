def combination(l, result=[]):
    for item in range(len(l)):
        cut_list = l[:item] + l[item + 1:]
        if len(cut_list) > 1:
            combination(cut_list, result)
        elif len(cut_list) == 1:
            result += cut_list
    return result


print(combination([3, 22, 10, 15, 32, 10, 5]))
