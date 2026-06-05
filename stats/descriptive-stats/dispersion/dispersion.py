"""Measures of dispersion (spread)."""

import math
from typing import List


def calculate_range(data: List[float]) -> float:
    """Difference between the maximum and minimum."""
    return max(data) - min(data)


def calculate_variance(data: List[float], sample: bool = False) -> float:
    """Population variance by default; pass sample=True to divide by n - 1."""
    mean = sum(data) / len(data)
    squared_diff = [(x - mean) ** 2 for x in data]
    divisor = len(data) - 1 if sample else len(data)
    if divisor <= 0:
        raise ValueError("sample variance requires at least 2 observations")
    return sum(squared_diff) / divisor


def calculate_standard_deviation(data: List[float], sample: bool = False) -> float:
    """Square root of the variance."""
    return math.sqrt(calculate_variance(data, sample=sample))


def calculate_coefficient_of_variation(data: List[float], sample: bool = False) -> float:
    """Standard deviation relative to the mean, as a percentage."""
    mean = sum(data) / len(data)
    if mean == 0:
        raise ValueError("coefficient of variation is undefined when the mean is 0")
    return (calculate_standard_deviation(data, sample=sample) / mean) * 100


def mean_absolute_deviation(data: List[float]) -> float:
    """Average absolute distance from the mean. Less sensitive to outliers than variance."""
    mean = sum(data) / len(data)
    return sum(abs(x - mean) for x in data) / len(data)


def median_absolute_deviation(data: List[float]) -> float:
    """Median of absolute deviations from the median. A robust measure of spread."""
    sorted_data = sorted(data)
    n = len(sorted_data)
    median = sorted_data[n // 2] if n % 2 else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    deviations = sorted(abs(x - median) for x in data)
    return deviations[n // 2] if n % 2 else (deviations[n // 2 - 1] + deviations[n // 2]) / 2


def percentile(data: List[float], p: float) -> float:
    """Linear-interpolation percentile (same as numpy default)."""
    if not 0 <= p <= 100:
        raise ValueError("p must be in [0, 100]")
    sorted_data = sorted(data)
    rank = (p / 100) * (len(sorted_data) - 1)
    lower = math.floor(rank)
    upper = math.ceil(rank)
    if lower == upper:
        return sorted_data[lower]
    return sorted_data[lower] + (sorted_data[upper] - sorted_data[lower]) * (rank - lower)


def z_scores(data: List[float], sample: bool = False) -> List[float]:
    """Standardized values: (x - mean) / std."""
    mean = sum(data) / len(data)
    std = calculate_standard_deviation(data, sample=sample)
    if std == 0:
        raise ValueError("z-scores are undefined when standard deviation is 0")
    return [(x - mean) / std for x in data]
