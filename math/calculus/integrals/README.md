# Integrals

Integration is the inverse of differentiation. It computes accumulated quantities — areas under curves, total displacement from velocity, probabilities under a density function.

## Concepts

- **Indefinite integral (antiderivative)** — a function whose derivative is the integrand, plus an integration constant.
- **Definite integral** — a number representing the signed area between the curve and the x-axis on `[a, b]`.
- **Fundamental theorem of calculus** — `integral_a^b f'(x) dx = f(b) - f(a)`. Connects derivatives and integrals.
- **Improper integral** — a definite integral with an infinite limit or an unbounded integrand.
- **Double integral** — integration over a 2D region. Computes volume, mass, or probability.
- **Area between curves** — `integral_a^b (f(x) - g(x)) dx` when `f >= g`.
- **Numerical integration** — methods like the trapezoid or Simpson's rule when no closed form exists.

## Files

- `integrals.py` — `indefinite`, `definite`, `double_integral`, `area_between_curves`, and a small `trapezoid_rule` numerical integrator.
- `main.py` — examples covering indefinite, definite, improper, and double integrals, plus a numerical comparison.

## Usage

```bash
python math/calculus/integrals/main.py
```
