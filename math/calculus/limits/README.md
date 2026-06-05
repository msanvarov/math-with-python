# Limits

Limits formalize what a function approaches as its input gets close to a target. They underpin the definitions of continuity, derivatives, and integrals.

## Concepts

- **Two-sided limit** — both the left- and right-hand limits exist and are equal.
- **One-sided limit** — approach the point from a specific direction (`+` or `-`).
- **Limit at infinity** — describes end behavior of a function.
- **Indeterminate forms** — expressions like `0/0` or `oo/oo` that require algebraic manipulation or L'Hopital's rule to evaluate.
- **Difference quotient** — `(f(x+h) - f(x)) / h`. Its limit as `h -> 0` defines the derivative.

## Files

- `limits.py` — thin wrappers around `sympy.limit`, plus helpers for the difference quotient and deriving derivatives from first principles.
- `main.py` — examples including the classic `sin(x)/x` limit and the derivative of `x^3` from the definition.

## Usage

```bash
python math/calculus/limits/main.py
```
