def sublist(input_list):
    output_list = []
    index = 0
    while index < len(input_list):
        if input_list[index] != 5:
            output_list.append(input_list[index])
            index += 1
        else:
            break
    return output_list
