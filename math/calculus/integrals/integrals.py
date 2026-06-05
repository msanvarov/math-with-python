"""Integration helpers built on sympy."""

import sympy as sym


def indefinite(expr, var):
    """Antiderivative (indefinite integral) of expr."""
    return sym.integrate(expr, var)


def definite(expr, var, a, b):
    """Definite integral of expr from a to b."""
    return sym.integrate(expr, (var, a, b))


def double_integral(expr, var1, a1, b1, var2, a2, b2):
    """Double integral over a rectangular region. Outer var first."""
    return sym.integrate(expr, (var2, a2, b2), (var1, a1, b1))


def area_between_curves(f, g, var, a, b):
    """Area between curves f and g on [a, b], assuming f >= g there."""
    return sym.integrate(f - g, (var, a, b))


def trapezoid_rule(f, var, a, b, n):
    """Numerical trapezoid-rule approximation with n subintervals."""
    a, b = sym.Rational(a), sym.Rational(b)
    h = (b - a) / n
    total = (f.subs(var, a) + f.subs(var, b)) / 2
    for i in range(1, n):
        total += f.subs(var, a + i * h)
    return float(h * total)
