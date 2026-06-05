import sympy as sym
from sympy.abc import x, y

from derivatives import (
    derivative,
    gradient,
    hessian,
    critical_points,
    tangent_line,
)

# Single-variable: derivative of sin(x) * exp(x)
f = sym.sin(x) * sym.exp(x)
print("f(x) =", f)
print("f'(x) =", derivative(f, x))
print("f''(x) =", derivative(f, x, 2))

# Critical points of x^3 - 3x
g = x**3 - 3 * x
print("Critical points of x^3 - 3x:", critical_points(g, x))

# Tangent line to x^2 at x = 1 (should be 2x - 1)
print("Tangent to x^2 at x=1:", sym.expand(tangent_line(x**2, x, 1)))

# Multivariable: gradient and Hessian of x^2 + xy + y^2
h_expr = x**2 + x * y + y**2
print("Gradient of x^2 + xy + y^2:", gradient(h_expr, [x, y]))
print("Hessian of x^2 + xy + y^2:")
sym.pprint(hessian(h_expr, [x, y]))

# Chain rule example: d/dx sin(x^2)
print("d/dx sin(x^2) =", derivative(sym.sin(x**2), x))

# Implicit differentiation example via sym.idiff: dy/dx of x^2 + y^2 = 1
expr = x**2 + y**2 - 1
print("Implicit dy/dx of x^2 + y^2 = 1:", sym.idiff(expr, y, x))
