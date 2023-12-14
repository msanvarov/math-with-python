from dispersion import calculate_range, calculate_variance, calculate_standard_deviation, calculate_coefficient_of_variation

data = [1.2, 2.5, 3.7, 4.1, 5.8, 6.3, 7.9]

range_value = calculate_range(data)
variance_value = calculate_variance(data)
standard_deviation_value = calculate_standard_deviation(data)
coefficient_of_variation_value = calculate_coefficient_of_variation(data)

print(f"Range: {range_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {standard_deviation_value}")
print(f"Coefficient of Variation: {coefficient_of_variation_value}%")
