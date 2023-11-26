import random
import numpy as np

def _random_sample(X, y, sample_size):
  data =[(i,j) for i,j in zip(X, y)]
  data_2= random.sample(data, sample_size)
  del data
  
  X1 = []
  y1 = []
  for t in data_2:
   X1.append(t[0])
   y1.append(t[1])
  
  del data_2
  X1 = np.array(X1)
  y1 = np.array(y1)
  return X1, y1


X_train=[ [1,1,1], [2,2,2],  [3,3,3], [4,4,4] ]
y_train =['a', 'b', 'c', 'd']

X1, y1 = _random_sample(X_train, y_train, 3)
