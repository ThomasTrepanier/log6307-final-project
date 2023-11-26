def get_closest_divisor(num, divisor):
    for i in range(num):
        if ( num % divisor > 0): 
            num = num + 1
    return num
