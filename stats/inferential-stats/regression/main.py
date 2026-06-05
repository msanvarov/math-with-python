import numpy as np

from regression import (
    simple_linear_regression,
    multiple_linear_regression,
    r_squared,
    residuals,
)

rng = np.random.default_rng(0)

# Simple linear regression: y = 2x + 1 + noise
x = np.linspace(0, 10, 100)
y = 2 * x + 1 + rng.normal(0, 1, size=x.size)

fit = simple_linear_regression(x, y)
print(f"simple regression: slope={fit.slope:.3f}, intercept={fit.intercept:.3f}")
print(f"R^2 = {fit.r_squared:.3f}, p = {fit.p_value:.3g}")
print(f"prediction at x=5: {fit.predict(5):.3f}")

# Multiple linear regression: y = 1 + 2*x1 - 3*x2 + noise
x1 = rng.normal(size=200)
x2 = rng.normal(size=200)
y_multi = 1 + 2 * x1 - 3 * x2 + rng.normal(0, 0.5, size=200)
X = np.column_stack([x1, x2])

coef = multiple_linear_regression(X, y_multi)
print(f"multi regression coefficients (intercept, b1, b2): {np.round(coef, 3)}")

# Diagnostic: R^2 and residual mean (should be ~0).
y_pred = coef[0] + X @ coef[1:]
print(f"R^2 = {r_squared(y_multi, y_pred):.3f}")
print(f"mean residual = {residuals(y_multi, y_pred).mean():.4f}")
