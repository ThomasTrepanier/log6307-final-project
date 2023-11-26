import random

def get_random_number(minval, maxval, none_probability):
    if random.random() < none_probability:
        return None
    else:
        return random.randint(minval, maxval)

def get_random_list(length, minval, maxval, none_probability):
    return [get_random_number(minval, maxval, none_probability)
            for _ in range(length)]

    
print(get_random_list(20, 0, 100, 0.2))
