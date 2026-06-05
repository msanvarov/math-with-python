import numpy as np

from correlation import pearson, spearman, kendall, correlation_matrix

rng = np.random.default_rng(0)

# Strong positive linear relationship: y = 2x + noise.
x = np.linspace(0, 10, 200)
y_linear = 2 * x + rng.normal(0, 1, size=x.size)

r, p = pearson(x, y_linear)
print(f"Linear data: Pearson r = {r:.3f}, p = {p:.3g}")

# Monotonic but non-linear: y = x^3 + noise. Spearman should beat Pearson.
y_cubic = x**3 + rng.normal(0, 50, size=x.size)
print(f"Cubic data: Pearson r = {pearson(x, y_cubic)[0]:.3f}")
print(f"Cubic data: Spearman rho = {spearman(x, y_cubic)[0]:.3f}")
print(f"Cubic data: Kendall tau = {kendall(x, y_cubic)[0]:.3f}")

# Uncorrelated data: both should be near zero.
y_random = rng.normal(0, 1, size=x.size)
print(f"Random data: Pearson r = {pearson(x, y_random)[0]:.3f}")

# Correlation matrix across three variables.
z = -0.5 * x + rng.normal(0, 0.5, size=x.size)
print("Correlation matrix (x, 2x+noise, -0.5x+noise):")
print(np.round(correlation_matrix(x, y_linear, z), 3))
