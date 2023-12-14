from distributions.random_data_generator import generate_uniform_data, generate_normal_data, generate_exponential_data

# Generate random data from a uniform distribution
uniform_data = generate_uniform_data(100, low=0, high=10)
print("Uniform Data:")
print(uniform_data)

# Generate random data from a normal distribution
normal_data = generate_normal_data(100, mean=0, std=1)
print("Normal Data:")
print(normal_data)

# Generate random data from an exponential distribution
exponential_data = generate_exponential_data(100, scale=1)
print("Exponential Data:")
print(exponential_data)
