"""Limit examples using sympy."""

import sympy as sym
from sympy.abc import x, h


def limit(expr, var, point, direction="+-"):
    """Compute a limit, optionally one-sided.

    direction: '+' (right), '-' (left), or '+-' (two-sided, default).
    """
    if direction == "+-":
        return sym.limit(expr, var, point)
    return sym.limit(expr, var, point, direction)


def difference_quotient(expr, var=x, h_sym=h):
    """Return the symbolic difference quotient (f(x+h) - f(x)) / h."""
    return (expr.subs(var, var + h_sym) - expr) / h_sym


def derivative_from_definition(expr, var=x, h_sym=h):
    """Derivative defined as the limit of the difference quotient as h -> 0."""
    return sym.simplify(sym.limit(difference_quotient(expr, var, h_sym), h_sym, 0))
