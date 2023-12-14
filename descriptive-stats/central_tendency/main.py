from central_tendency import compute_mean, compute_median, compute_mode

# Example data
data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

# Compute mean
mean = compute_mean(data)
print(f"Mean: {mean}")

# Compute median
median = compute_median(data)
print(f"Median: {median}")

# Compute mode
modes = compute_mode(data)
print(f"Mode(s): {modes}")
