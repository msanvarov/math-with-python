import sympy as sym
from sympy.abc import x

from limits import limit, difference_quotient, derivative_from_definition

# Basic two-sided limit: lim x->2 of (x^2 - 4) / (x - 2)
expr = (x**2 - 4) / (x - 2)
print("lim x->2 (x^2 - 4)/(x - 2) =", limit(expr, x, 2))

# Limit at infinity: lim x->oo of (3x^2 + x) / (x^2 - 1)
expr = (3 * x**2 + x) / (x**2 - 1)
print("lim x->oo (3x^2 + x)/(x^2 - 1) =", limit(expr, x, sym.oo))

# One-sided limit: lim x->0+ of 1/x = +oo, lim x->0- of 1/x = -oo
print("lim x->0+ 1/x =", limit(1 / x, x, 0, "+"))
print("lim x->0- 1/x =", limit(1 / x, x, 0, "-"))

# Famous trigonometric limit
print("lim x->0 sin(x)/x =", limit(sym.sin(x) / x, x, 0))

# Derivative from first principles via the difference quotient
f = x**3
print("Difference quotient for x^3:", sym.simplify(difference_quotient(f)))
print("Derivative of x^3 from definition:", derivative_from_definition(f))
