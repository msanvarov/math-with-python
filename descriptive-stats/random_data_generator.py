import numpy as np

def generate_uniform_data(size, low=0, high=1):
    """
    Generate random data from a uniform distribution.

    Parameters:
    - size: int, the number of random data points to generate.
    - low: float, the lower bound of the distribution (default: 0).
    - high: float, the upper bound of the distribution (default: 1).

    Returns:
    - ndarray: 1-D array of random data points.
    """
    return np.random.uniform(low, high, size)

def generate_normal_data(size, mean=0, std=1):
    """
    Generate random data from a normal distribution.

    Parameters:
    - size: int, the number of random data points to generate.
    - mean: float, the mean of the distribution (default: 0).
    - std: float, the standard deviation of the distribution (default: 1).

    Returns:
    - ndarray: 1-D array of random data points.
    """
    return np.random.normal(mean, std, size)

def generate_exponential_data(size, scale=1):
    """
    Generate random data from an exponential distribution.

    Parameters:
    - size: int, the number of random data points to generate.
    - scale: float, the scale parameter of the distribution (default: 1).

    Returns:
    - ndarray: 1-D array of random data points.
    """
    return np.random.exponential(scale, size)
