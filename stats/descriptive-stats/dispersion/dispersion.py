import math
from typing import List

def calculate_range(data: List[float]) -> float:
    """Calculate the range of a given dataset."""
    return max(data) - min(data)

def calculate_variance(data: List[float]) -> float:
    """Calculate the variance of a given dataset."""
    mean = sum(data) / len(data)
    squared_diff = [(x - mean) ** 2 for x in data]
    return sum(squared_diff) / len(data)

def calculate_standard_deviation(data: List[float]) -> float:
    """Calculate the standard deviation of a given dataset."""
    variance = calculate_variance(data)
    return math.sqrt(variance)

def calculate_coefficient_of_variation(data: List[float]) -> float:
    """Calculate the coefficient of variation of a given dataset."""
    mean = sum(data) / len(data)
    standard_deviation = calculate_standard_deviation(data)
    return (standard_deviation / mean) * 100
