"""Simple and multiple linear regression."""

from dataclasses import dataclass

import numpy as np
from scipy import stats


@dataclass
class SimpleRegressionResult:
    slope: float
    intercept: float
    r_squared: float
    p_value: float
    std_err: float

    def predict(self, x):
        return self.slope * np.asarray(x) + self.intercept


def simple_linear_regression(x, y):
    """Fit y = slope * x + intercept via least squares."""
    result = stats.linregress(x, y)
    return SimpleRegressionResult(
        slope=float(result.slope),
        intercept=float(result.intercept),
        r_squared=float(result.rvalue) ** 2,
        p_value=float(result.pvalue),
        std_err=float(result.stderr),
    )


def multiple_linear_regression(X, y):
    """Fit y = X @ beta + epsilon via the normal equations.

    Returns coefficients with an intercept term as the first entry.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    X_with_intercept = np.column_stack([np.ones(X.shape[0]), X])
    coef, *_ = np.linalg.lstsq(X_with_intercept, y, rcond=None)
    return coef


def r_squared(y_true, y_pred):
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - y_true.mean()) ** 2)
    return 1 - ss_res / ss_tot


def residuals(y_true, y_pred):
    return np.asarray(y_true) - np.asarray(y_pred)
