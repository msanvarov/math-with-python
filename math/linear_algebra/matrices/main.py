import numpy as np

from matrices import (
    matmul,
    transpose,
    determinant,
    inverse,
    rank,
    trace,
    solve_linear_system,
)

A = np.array([[1, 2], [3, 4]], dtype=float)
B = np.array([[5, 6], [7, 8]], dtype=float)

print("A @ B =\n", matmul(A, B))
print("A.T =\n", transpose(A))
print("det(A) =", determinant(A))
print("rank(A) =", rank(A))
print("trace(A) =", trace(A))
print("A^-1 =\n", inverse(A))
print("A @ A^-1 =\n", np.round(matmul(A, inverse(A)), 6))

# Solve a linear system: 2x + y = 5, x + 3y = 10  ->  (x, y) = (1, 3)
M = np.array([[2, 1], [1, 3]], dtype=float)
b = np.array([5, 10], dtype=float)
print("Solution to Mx = b:", solve_linear_system(M, b))

# Singular matrix: determinant is 0 -> not invertible
S = np.array([[1, 2], [2, 4]], dtype=float)
print("det(singular matrix) =", determinant(S))
print("rank(singular matrix) =", rank(S))
