"""Matrix operations using numpy."""

import numpy as np


def matmul(A, B):
    """Matrix product A @ B."""
    return np.asarray(A) @ np.asarray(B)


def transpose(A):
    return np.asarray(A).T


def determinant(A):
    return float(np.linalg.det(A))


def inverse(A):
    """Matrix inverse. Raises if A is singular."""
    return np.linalg.inv(A)


def rank(A):
    return int(np.linalg.matrix_rank(A))


def trace(A):
    return float(np.trace(A))


def solve_linear_system(A, b):
    """Solve Ax = b for x (unique-solution case)."""
    return np.linalg.solve(A, b)


def lu_decomposition(A):
    """LU decomposition via scipy. Returns (P, L, U)."""
    from scipy.linalg import lu

    return lu(np.asarray(A, dtype=float))
