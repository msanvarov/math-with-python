import numpy as np

from hypothesis_testing import (
    one_sample_t_test,
    two_sample_t_test,
    paired_t_test,
    chi_square_independence,
    shapiro_wilk,
    mann_whitney_u,
)

rng = np.random.default_rng(42)

# One-sample t-test: is the sample mean = 0?
data = rng.normal(loc=0.3, scale=1, size=100)
print("one-sample t-test (H0: mu = 0):", one_sample_t_test(data, popmean=0))

# Two-sample t-test: do two groups have different means?
group_a = rng.normal(loc=0, scale=1, size=50)
group_b = rng.normal(loc=0.5, scale=1, size=50)
print("two-sample t-test (Welch):", two_sample_t_test(group_a, group_b))

# Paired t-test: before vs after an intervention on the same subjects.
before = rng.normal(loc=100, scale=10, size=30)
after = before + rng.normal(loc=-3, scale=5, size=30)
print("paired t-test (before vs after):", paired_t_test(before, after))

# Chi-square test of independence on a 2x2 contingency table.
table = [[20, 30], [15, 35]]
print("chi-square independence:", chi_square_independence(table))

# Shapiro-Wilk normality test.
print("Shapiro-Wilk on normal data:", shapiro_wilk(rng.normal(size=100)))
print("Shapiro-Wilk on exponential data:", shapiro_wilk(rng.exponential(size=100)))

# Mann-Whitney U test (non-parametric two-sample).
print("Mann-Whitney U:", mann_whitney_u(group_a, group_b))
