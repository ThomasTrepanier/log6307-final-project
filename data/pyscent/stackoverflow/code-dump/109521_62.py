def count_zeros(number:int) -> int:

    if number==0:
        return 1

    number_list = list(str(number))

    is_zero = True
    zero_count = 0

    while is_zero:
        if int(number_list.pop())==0:
            zero_count += 1
        else:
            is_zero = False

    return zero_count
