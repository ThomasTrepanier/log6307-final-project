import numpy as np

def zero_off_diag_covariance(nb_of_samples, variance=1):
    return np.eye(nb_of_samples) * variance
