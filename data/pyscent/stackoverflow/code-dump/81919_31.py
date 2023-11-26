def valid(num, count=0):
    num, r = divmod(num, 10) # extract the last digit (r)
    if num == 0:             # we exhausted the number
        return count%2==0    # is there an even number of zeros?
    else:
        return valid(num, count=count+int(r==0))
