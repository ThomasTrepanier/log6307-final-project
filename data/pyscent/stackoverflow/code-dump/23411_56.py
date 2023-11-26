import numpy as np

def convert_to_array(dictionary):
    '''Converts lists of values in a dictionary to numpy arrays'''
    return {k:np.array(v) for k, v in dictionary.items()}

d = {
    'date-1': [1.23, 2.34, 3.45, 5.67],
    'date-2': [54.47, 45.22, 22.33, 54.89],
    'date-3': [0.33, 0.589, 12.654, 4.36]
}

print(convert_to_array(d))
# {'date-1': array([1.23, 2.34, 3.45, 5.67]), 'date-2': array([54.47, 45.22, 22.33, 54.89]), 'date-3': array([ 0.33 ,  0.589, 12.654,  4.36 ])}
