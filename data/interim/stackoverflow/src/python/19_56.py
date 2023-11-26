def digitOfLife(date):
    sum_ = 0
    if (len(date) > 8):
        print("Input data too long")
        return
    else:
        date_list = []
        for char in date:
            date_list.append(int(char))

        sum_ = sum(date_list) # calculate the sum of list of digits
        while len(str(sum_)) > 1: # repeat while the sum has more than 1 digit
            sum_ = sum(date_list)
            date_list = [int(x) for x in str(sum_)]

    return sum_
