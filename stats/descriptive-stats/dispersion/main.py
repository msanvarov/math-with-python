from dispersion import (
    calculate_range,
    calculate_variance,
    calculate_standard_deviation,
    calculate_coefficient_of_variation,
    mean_absolute_deviation,
    median_absolute_deviation,
    percentile,
    z_scores,
)

data = [1.2, 2.5, 3.7, 4.1, 5.8, 6.3, 7.9]

print(f"Range: {calculate_range(data)}")
print(f"Population variance: {calculate_variance(data):.4f}")
print(f"Sample variance:     {calculate_variance(data, sample=True):.4f}")
print(f"Standard deviation:  {calculate_standard_deviation(data):.4f}")
print(f"Coefficient of variation: {calculate_coefficient_of_variation(data):.2f}%")
print(f"Mean absolute deviation:   {mean_absolute_deviation(data):.4f}")
print(f"Median absolute deviation: {median_absolute_deviation(data):.4f}")

print(f"25th percentile: {percentile(data, 25):.3f}")
print(f"75th percentile: {percentile(data, 75):.3f}")
print(f"95th percentile: {percentile(data, 95):.3f}")

print("Z-scores:", [round(z, 3) for z in z_scores(data)])
