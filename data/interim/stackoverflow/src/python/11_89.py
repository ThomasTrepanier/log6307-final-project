import numpy as np
def string_to_matrix(str_in):
   str_in_split = str_in.split()
   numbers = list(map(int, str_in_split))
   size = r_shape = int(np.sqrt(len(numbers)))
   return np.array(numbers).reshape(r_shape, r_shape)
