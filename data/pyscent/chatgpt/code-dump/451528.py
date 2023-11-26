import numpy as np

def max_nonzero_per_row(matrices, cutoff):
    max_counts = []
    for matrix in matrices:
        np.fill_diagonal(matrix, 0)  # Set diagonal entries to zero
        matrix = np.where(np.abs(matrix) >= cutoff, matrix, 0)  # Apply cutoff
        row_counts = np.count_nonzero(matrix, axis=1)  # Count non-zero entries in each row
        max_counts.append(np.max(row_counts))  # Get max count for this matrix
    return max_counts
