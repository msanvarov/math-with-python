# Matrices

Matrices represent linear transformations and systems of linear equations. They are the workhorse of numerical linear algebra.

## Concepts

- **Matrix multiplication** — composition of linear transformations. Not commutative in general.
- **Transpose** — flip rows and columns. `(A^T)_ij = A_ji`.
- **Determinant** — a scalar measuring how the transformation scales volume. Zero when the matrix is singular (non-invertible).
- **Inverse** — `A^{-1}` such that `A A^{-1} = I`. Exists only when `det(A) != 0`.
- **Rank** — the number of linearly independent rows (or columns).
- **Trace** — the sum of diagonal entries. Invariant under change of basis.
- **Solving Ax = b** — when `A` is invertible, the solution is `x = A^{-1} b`. Numerically, prefer `numpy.linalg.solve`.
- **LU decomposition** — factor `A = P L U` to make repeated solves cheap.

## Files

- `matrices.py` — `matmul`, `transpose`, `determinant`, `inverse`, `rank`, `trace`, `solve_linear_system`, `lu_decomposition`.
- `main.py` — examples including solving a 2x2 system and inspecting a singular matrix.

## Usage

```bash
python math/linear_algebra/matrices/main.py
```
