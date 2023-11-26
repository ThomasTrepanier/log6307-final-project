import random

def generate_n_lists(num_of_lists, num_of_elements, value_from=0, value_to=100):
    s = random.sample(range(value_from, value_to + 1), num_of_lists * num_of_elements)
    return [s[i*num_of_elements:(i+1)*num_of_elements] for i in range(num_of_lists)]

print(generate_n_lists(2, 5, 0, 20))    # generate 2 lists, each 5 elements, values are from 0 to 20
