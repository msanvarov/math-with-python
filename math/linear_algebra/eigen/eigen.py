"""Eigenvalues, eigenvectors, and related decompositions."""

import numpy as np


def eigendecomposition(A):
    """Return (eigenvalues, eigenvectors). Columns of eigenvectors are unit-length."""
    return np.linalg.eig(np.asarray(A, dtype=float))


def spectral_radius(A):
    """Largest absolute eigenvalue."""
    eigvals, _ = eigendecomposition(A)
    return float(np.max(np.abs(eigvals)))


def is_diagonalizable(A, tol=1e-10):
    """True if A has a full set of linearly independent eigenvectors."""
    _, vecs = eigendecomposition(A)
    return np.linalg.matrix_rank(vecs, tol=tol) == np.asarray(A).shape[0]


def svd(A):
    """Singular value decomposition: A = U S V^T."""
    return np.linalg.svd(np.asarray(A, dtype=float))


def power_iteration(A, num_iter=100, tol=1e-10):
    """Estimate the dominant eigenvalue/eigenvector via power iteration."""
    A = np.asarray(A, dtype=float)
    b = np.random.rand(A.shape[1])
    b /= np.linalg.norm(b)
    eigval = 0.0
    for _ in range(num_iter):
        b_next = A @ b
        b_next /= np.linalg.norm(b_next)
        eigval_next = float(b_next @ A @ b_next)
        if abs(eigval_next - eigval) < tol:
            return eigval_next, b_next
        b, eigval = b_next, eigval_next
    return eigval, b
