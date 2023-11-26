import numpy as np

def sample_multivariate_normal(mean, cov, size=1):
    # Step 1: Compute the Cholesky decomposition of the covariance matrix
    L = np.linalg.cholesky(cov)

    # Step 2: Generate uncorrelated random samples
    uncorrelated_samples = np.random.normal(size=(size, mean.shape[0]))

    # Step 3: Create correlated samples
    correlated_samples = uncorrelated_samples @ L.T

    # Step 4: Add the mean
    samples = correlated_samples + mean

    return samples

mean = np.array([0, 0])
cov = np.array([
    [1, 0.8],
    [0.8, 1]
])

samples = sample_multivariate_normal(mean, cov, size=1000)

# Now `samples` is a 1000x2 array where each row is a sample from the multivariate normal distribution.
