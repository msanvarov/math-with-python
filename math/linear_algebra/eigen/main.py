import numpy as np

from eigen import (
    eigendecomposition,
    spectral_radius,
    is_diagonalizable,
    svd,
    power_iteration,
)

A = np.array([[4, 1], [2, 3]], dtype=float)

eigvals, eigvecs = eigendecomposition(A)
print("eigenvalues:", eigvals)
print("eigenvectors (columns):\n", eigvecs)

# Verify A v = lambda v for the first eigenpair.
v0 = eigvecs[:, 0]
print("A v0:", A @ v0)
print("lambda0 v0:", eigvals[0] * v0)

print("spectral radius:", spectral_radius(A))
print("diagonalizable?", is_diagonalizable(A))

# SVD: every matrix has one. Reconstruct A from U S V^T.
U, S, Vt = svd(A)
print("singular values:", S)
print("reconstructed A:\n", np.round(U @ np.diag(S) @ Vt, 6))

# Power iteration converges to the dominant eigenpair.
np.random.seed(0)
dominant_val, dominant_vec = power_iteration(A)
print(f"power iteration dominant eigenvalue: {dominant_val:.6f}")
