"""Derivative helpers built on sympy."""

import sympy as sym


def derivative(expr, var, order=1):
    """nth-order derivative of expr with respect to var."""
    return sym.diff(expr, var, order)


def partial_derivative(expr, var):
    """Partial derivative — same as sym.diff but named for clarity in multivariable contexts."""
    return sym.diff(expr, var)


def gradient(expr, vars):
    """Gradient vector: list of partial derivatives wrt each var."""
    return [sym.diff(expr, v) for v in vars]


def hessian(expr, vars):
    """Hessian matrix of second partials. Returns a sympy Matrix."""
    return sym.Matrix([[sym.diff(expr, vi, vj) for vj in vars] for vi in vars])


def critical_points(expr, var):
    """Solve f'(x) = 0 for critical points of a single-variable function."""
    return sym.solve(sym.diff(expr, var), var)


def tangent_line(expr, var, a):
    """Tangent line to f at x = a: y = f(a) + f'(a) * (x - a)."""
    f_a = expr.subs(var, a)
    fprime_a = sym.diff(expr, var).subs(var, a)
    return f_a + fprime_a * (var - a)
