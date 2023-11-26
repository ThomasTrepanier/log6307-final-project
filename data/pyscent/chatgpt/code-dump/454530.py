import numpy as np
import scipy.sparse

def max_nonzero_per_row(matrices, cutoff):
    max_counts = []
    for matrix in matrices:
        # Check if the matrix is sparse
        if scipy.sparse.issparse(matrix):
            matrix = matrix.copy()  # Ensure we don't modify the original matrix
            matrix.data[np.abs(matrix.data) < cutoff] = 0  # Apply cutoff
            matrix.setdiag(0)  # Set diagonal entries to zero
            row_counts = matrix.getnnz(axis=1)  # Count non-zero entries in each row
        else:
            mask = np.abs(matrix) >= cutoff  # Create a mask of entries above the cutoff
            np.fill_diagonal(mask, 0)  # Set diagonal entries to zero
            row_counts = np.count_nonzero(mask, axis=1)  # Count non-zero entries in each row
        max_counts.append(np.max(row_counts))  # Get max count for this matrix
    return max_counts
