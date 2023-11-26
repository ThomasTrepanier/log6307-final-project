numbers = [  1, 3, 11,  12,  14,  15,  16, 3, 4, 6]

def longest(numbers):
    max, count_ = 1, 1
    start_idx, end_idx = 0, 0
    for i in range(len(numbers)-1):
        # if difference between number and his follower is 1,they are in sequence
        if numbers[i+1]-numbers[i] ==1:
            count_ = count_+1
        else:
            if count_ > max :
                max = count_
                end_idx = i
                start_idx = i+1 - max
            # Reset counter
            count_ = 1
    return (start_idx,end_idx,max)


print (longest(numbers))
