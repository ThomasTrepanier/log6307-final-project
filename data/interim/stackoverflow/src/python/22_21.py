import numpy as np
np.random.seed(42)

# Function to generate a random point on a uniform sphere
# (relying on https://stackoverflow.com/a/33977530/8565438)

def randompoint(ndim=3):
    vec = np.random.randn(ndim,1)
    vec /= np.linalg.norm(vec, axis=0)
    return vec

# Give the length of each axis (example values):

a, b, c = 1, 2, 4

# Function to scale up generated points using the function `f` mentioned above:

f = lambda x,y,z : np.multiply(np.array([a,b,c]),np.array([x,y,z]))

# Keep the point with probability `mu(x,y,z)/mu_max`, ie

def keep(x, y, z, a=a, b=b, c=c):
    mu_xyz = ((a * c * y) ** 2 + (a * b * z) ** 2 + (b * c * x) ** 2) ** 0.5
    return mu_xyz / (b * c) > np.random.uniform(low=0.0, high=1.0)

# Generate points until we have, let's say, 1000 points:

n = 1000
points = []
while len(points) < n:
    [x], [y], [z] = randompoint()
    if keep(x, y, z):
        points.append(f(x, y, z))
