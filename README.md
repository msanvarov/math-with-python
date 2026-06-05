# Math with Python

A growing collection of small, focused modules that explore mathematics and statistics concepts in Python. Each topic lives in its own folder with a short README, runnable code, and (where useful) tests and rendered LaTeX output.

## Setup

The project uses [Poetry](https://python-poetry.org/) for dependency management.

```bash
poetry install
poetry shell
```

Dependencies: `numpy`, `scipy`, `matplotlib`, `statsmodels`, `sympy`, and `pytest` (dev).

## Math

Symbolic math with `sympy` and numerical work with `numpy`/`scipy`.

### Algebra

| Topic | Description |
| --- | --- |
| [Algebra properties](math/algebra/properties/README.md) | Associative, commutative, and distributive properties demonstrated symbolically. |
| [Polynomials](math/algebra/polynomials/README.md) | Addition, multiplication, division, and factoring of polynomials using `sympy.Poly`. |

### Calculus

| Topic | Description |
| --- | --- |
| [Limits](math/calculus/limits/README.md) | One- and two-sided limits, limits at infinity, and derivatives from first principles. |
| [Derivatives](math/calculus/derivatives/README.md) | Single- and multivariable differentiation, gradients, Hessians, tangent lines. |
| [Integrals](math/calculus/integrals/README.md) | Indefinite, definite, improper, and double integrals, plus a numerical comparison. |

### Linear algebra

| Topic | Description |
| --- | --- |
| [Vectors](math/linear_algebra/vectors/README.md) | Dot/cross products, norms, projections, and angles. |
| [Matrices](math/linear_algebra/matrices/README.md) | Multiplication, determinants, inverses, ranks, and solving linear systems. |
| [Eigenvalues & SVD](math/linear_algebra/eigen/README.md) | Eigendecompositions, spectral radius, SVD, and power iteration. |

## Statistics

### Descriptive statistics

| Topic | Description |
| --- | --- |
| [Central tendency](stats/descriptive-stats/central_tendency/README.md) | Mean, median, mode, plus weighted, geometric, harmonic, and trimmed means. |
| [Dispersion](stats/descriptive-stats/dispersion/README.md) | Range, variance, standard deviation, CV, MAD, percentiles, z-scores. |
| [Interquartile range (IQR)](stats/descriptive-stats/iqr/README.md) | A robust measure of spread based on the middle 50% of the data. |
| [QQ plots](stats/descriptive-stats/qq_plots/README.md) | Visual check of how well a dataset matches a theoretical distribution. |
| [Random data generation](stats/descriptive-stats/random_data/README.md) | Sampling from uniform, normal, exponential, binomial, Poisson, lognormal, and beta distributions. |

### Inferential statistics

| Topic | Description |
| --- | --- |
| [Correlation](stats/inferential-stats/correlation/README.md) | Pearson, Spearman, Kendall, and covariance/correlation matrices. |
| [Hypothesis testing](stats/inferential-stats/hypothesis_testing/README.md) | t-tests, chi-square independence, Shapiro-Wilk, Mann-Whitney U. |
| [Linear regression](stats/inferential-stats/regression/README.md) | Simple and multiple linear regression with R^2 and residual diagnostics. |

## Running a module

Each module ships with a `main.py` you can run directly:

```bash
python stats/descriptive-stats/central_tendency/main.py
python math/calculus/derivatives/main.py
python math/linear_algebra/eigen/main.py
```

The algebra modules also write rendered LaTeX to `.html` files alongside the code — open them in a browser to see formatted expressions.

## Tests

```bash
pytest
```

## Repository layout

```
math/
  algebra/        properties, polynomials
  calculus/       limits, derivatives, integrals
  linear_algebra/ vectors, matrices, eigen
stats/
  descriptive-stats/  central_tendency, dispersion, iqr, qq_plots, random_data
  inferential-stats/  correlation, hypothesis_testing, regression
```
