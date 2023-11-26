#You can rewrite matrix A as

[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1],   * a + 
 [0, 0, 0],
 [0, 0, 0]]

[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0],
 [1, 1, 0],
 [0, 0, 1]]


#Define your loss function
def lossf(M):
    Y = np.array([0.4,0.4,0.2,0.1,0.05])
    a,b,c,d = M
    A = np.array([[1,0,0],[0,1,0],[0,0,1],[0,0,0],[0,0,0]])*a
    A = A + np.array([[0,0,0],[0,0,0],[0,0,0],[1,1,0],[0,0,1]])
    y = A.dot(np.array([b,c,d]).T)
    return np.sum((Y - y)**2)

#An extra function to calculate the matrix in the end
def mat(M):
    Y = np.array([0.4,0.4,0.2,0.1,0.05])
    a,b,c,d = M
    A = np.array([[1,0,0],[0,1,0],[0,0,1],[0,0,0],[0,0,0]])*a
    A = A + np.array([[0,0,0],[0,0,0],[0,0,0],[1,1,0],[0,0,1]])
    y = A.dot(np.array([b,c,d]).T)
    return y

import numpy as np
from scipy.optimize import least_squares

#this takes some time ** does 100000 rounds which can be changed
#[0,0,0,0] = random initialization of parameters
result = least_squares(lossf,[0,0,0,0], verbose=1, max_nfev = 100000)


result.x #result for parameter estimate
[6.97838023, 0.05702932, 0.05702932, 0.02908934] # run code and 

mat(result.x)
#The non-linear fit
[0.39797228, 0.39797228, 0.20299648, 0.11405864, 0.02908934]

#Orignal 
[0.4,0.4,0.2,0.1,0.05]


#Also results for other matrix
#This requires changing the loss function
#For a permanent solution you can write a flexible loss function
Y = np.array([0.4,0.4,0.2,0.1])
result = least_squares(lossf,[0,0,0,0], verbose=1, max_nfev = 10000)


result.x
[7.14833526, 0.0557289 , 0.0557289 , 0.02797854]

mat(result.x)
[0.39836889, 0.39836889, 0.2       , 0.11145781]
#The results are very close to analytical solution




