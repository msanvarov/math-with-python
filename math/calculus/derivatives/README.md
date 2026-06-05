# Derivatives

The derivative of a function measures its instantaneous rate of change. It's the slope of the tangent line at a point and the building block of optimization, physics, and machine learning.

## Concepts

- **Derivative** — `f'(x) = lim_{h -> 0} (f(x+h) - f(x)) / h`.
- **Higher-order derivatives** — `f''`, `f'''`, etc. The second derivative describes concavity.
- **Partial derivative** — derivative of a multivariable function with respect to one variable, holding the others constant.
- **Gradient** — vector of partial derivatives. Points in the direction of steepest ascent.
- **Hessian** — matrix of second partial derivatives. Encodes local curvature.
- **Critical points** — where `f'(x) = 0`. Candidates for local maxima, minima, or saddle points.
- **Tangent line** — `y = f(a) + f'(a) * (x - a)`. The linear approximation of `f` at `a`.
- **Implicit differentiation** — find `dy/dx` from an equation that isn't solved for `y`.

## Files

- `derivatives.py` — `derivative`, `partial_derivative`, `gradient`, `hessian`, `critical_points`, `tangent_line`.
- `main.py` — single- and multivariable examples, plus implicit differentiation of the unit circle.

## Usage

```bash
python math/calculus/derivatives/main.py
```
