import numpy as np

list_a = np.array([[0,1], [2,2], [5,4], [3,6], [4,2]])
list_b = np.array([[0,1],[5,4]])

def run_euc(list_a,list_b):
    return np.array([[ np.linalg.norm(i-j) for j in list_b] for i in list_a])

print(run_euc(list_a, list_b))
