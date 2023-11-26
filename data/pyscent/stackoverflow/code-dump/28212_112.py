@return_list
def sublist(x):
    for num in x:
        if num == 5:
            # we need to stop; break out of the for loop
            break
        # output the next number
        yield num
