import math

def stirling_lower_bound(k, X):
    term1 = (2 * math.pi * k) ** (1 / (2 * k))
    term2 = (k / math.e) ** (k / k)
    term3 = math.exp(1 / (12 * k + 1) / k)
    lower_bound = term1 * term2 * term3
    return lower_bound

def stirling_upper_bound(k, X):
    term1 = (2 * math.pi * k) ** (1 / (2 * k))
    term2 = (k / math.e) ** (k / k)
    term3 = math.exp(1 / (12 * k) / k)
    upper_bound = term1 * term2 * term3
    return upper_bound

def calculate_bounds(k, X):
    lower = stirling_lower_bound(k, X)
    upper = stirling_upper_bound(k, X)
    return lower, upper

# Example usage:
k = 5
X = 1.5
lower_bound, upper_bound = calculate_bounds(k, X)
print(f"For k = {k} and X = {X}:")
print(f"Lower Bound (n >=): {lower_bound}")
print(f"Upper Bound (n <=): {upper_bound}")
