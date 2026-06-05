# Eigenvalues, Eigenvectors, and SVD

For a square matrix `A`, an **eigenvector** `v` satisfies `A v = lambda v` for some scalar **eigenvalue** `lambda`. Eigendecompositions reveal the natural axes along which a linear transformation acts by pure stretching.

## Concepts

- **Eigenvalue / eigenvector** — `(A - lambda I) v = 0` for non-zero `v`.
- **Characteristic polynomial** — `det(A - lambda I) = 0`. Its roots are the eigenvalues.
- **Spectral radius** — the largest absolute eigenvalue. Governs convergence of iterative methods.
- **Diagonalizability** — a matrix is diagonalizable iff it has a full set of linearly independent eigenvectors.
- **Singular Value Decomposition (SVD)** — `A = U S V^T` exists for *every* matrix, not just square ones. Foundational for PCA, low-rank approximation, and pseudoinverses.
- **Power iteration** — a simple algorithm that converges to the dominant eigenvector by repeated multiplication.

## Files

- `eigen.py` — `eigendecomposition`, `spectral_radius`, `is_diagonalizable`, `svd`, `power_iteration`.
- `main.py` — verify `A v = lambda v`, reconstruct `A` from its SVD, and run power iteration.

## Usage

```bash
python math/linear_algebra/eigen/main.py
```
