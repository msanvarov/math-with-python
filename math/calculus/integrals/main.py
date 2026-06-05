import sympy as sym
from sympy.abc import x, y

from integrals import (
    indefinite,
    definite,
    double_integral,
    area_between_curves,
    trapezoid_rule,
)

# Indefinite integral
print("integral of x^2 dx =", indefinite(x**2, x))
print("integral of e^x sin(x) dx =", indefinite(sym.exp(x) * sym.sin(x), x))

# Definite integral
print("integral of x^2 from 0 to 1 =", definite(x**2, x, 0, 1))
print("integral of sin(x) from 0 to pi =", definite(sym.sin(x), x, 0, sym.pi))

# Improper integral
print("integral of e^-x from 0 to oo =", definite(sym.exp(-x), x, 0, sym.oo))

# Double integral over the unit square
print("double integral of x*y on [0,1]x[0,1] =", double_integral(x * y, x, 0, 1, y, 0, 1))

# Area between y = x and y = x^2 on [0, 1]
print("area between x and x^2 on [0, 1] =", area_between_curves(x, x**2, x, 0, 1))

# Numerical check via trapezoid rule
exact = float(definite(x**2, x, 0, 1))
approx = trapezoid_rule(x**2, x, 0, 1, 100)
print(f"x^2 on [0, 1]: exact={exact:.6f}, trapezoid(n=100)={approx:.6f}")
