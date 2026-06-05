# Linear Regression

Linear regression fits a straight line (or hyperplane) through observed data by minimizing the sum of squared residuals. It is both a forecasting tool and a way to quantify how much a predictor matters.

## Concepts

- **Simple linear regression** — one predictor: `y = beta_0 + beta_1 x + epsilon`.
- **Multiple linear regression** — many predictors: `y = X beta + epsilon`.
- **Least squares** — choose `beta` to minimize `sum (y_i - y_hat_i)^2`. Closed-form solution: `beta = (X^T X)^{-1} X^T y`.
- **R^2 (coefficient of determination)** — fraction of variance in `y` explained by the model. 1 is perfect, 0 means the model is no better than predicting the mean.
- **Residuals** — `y - y_hat`. Should look like random noise with no pattern if the model is appropriate.
- **p-value (for the slope)** — tests whether the slope is statistically distinguishable from zero.

## Files

- `regression.py` — `simple_linear_regression`, `multiple_linear_regression`, `r_squared`, `residuals`.
- `main.py` — fits both simple and multivariate models on simulated data and recovers the known coefficients.

## Usage

```bash
python stats/inferential-stats/regression/main.py
```
