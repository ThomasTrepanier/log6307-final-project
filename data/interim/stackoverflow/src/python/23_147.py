from itertools import combinations 

def is_sum_of_n_numbers(data ,target_value, num_elem):
    """Returns 'True' if any combinatin of 'num_elem'ents 
    from 'data' sums to 'target_value'"""
    return any(sum(x)==target_value for x in combinations(data, num_elem))

def find_sum_in_combination(data, target_value, num_elem):
    """Returns all combinations of 'num_elem'ent-tuples from 'data' 
    that sums to 'target_value'"""
    return [x for x in combinations(data,num_elem) if sum(x) == target_value]
