from central_tendency import (
    compute_mean,
    compute_median,
    compute_mode,
    weighted_mean,
    geometric_mean,
    harmonic_mean,
    trimmed_mean,
    midrange,
)

data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

print(f"Mean: {compute_mean(data)}")
print(f"Median: {compute_median(data)}")
print(f"Mode(s): {compute_mode(data)}")
print(f"Midrange: {midrange(data)}")

# Weighted mean: a grade average where exams matter more than homework.
grades = [85, 90, 78]
weights = [0.5, 0.3, 0.2]
print(f"Weighted mean (grades): {weighted_mean(grades, weights):.2f}")

# Geometric mean: average growth across 3 years of 5%, 10%, 15%.
growth_factors = [1.05, 1.10, 1.15]
print(f"Geometric mean (growth factors): {geometric_mean(growth_factors):.4f}")

# Harmonic mean: average speed when traveling equal distances at 30 and 60 mph.
speeds = [30, 60]
print(f"Harmonic mean (speeds): {harmonic_mean(speeds):.2f}")

# Trimmed mean: same data with an outlier added.
noisy = data + [1000]
print(f"Mean with outlier: {compute_mean(noisy):.2f}")
print(f"10% trimmed mean with outlier: {trimmed_mean(noisy, 0.1):.2f}")
