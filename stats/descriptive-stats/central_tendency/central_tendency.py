"""Measures of central tendency."""

import math
from collections import Counter
from typing import List, Optional


def compute_mean(data: List[float]) -> float:
    """Arithmetic mean."""
    return sum(data) / len(data)


def compute_median(data: List[float]) -> float:
    """Middle value of the sorted data; average of the two middles when n is even."""
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def compute_mode(data: List[float]) -> List[float]:
    """Value(s) that appear most often. Returns a list to handle multimodal data."""
    counter = Counter(data)
    max_count = max(counter.values())
    return [num for num, count in counter.items() if count == max_count]


def weighted_mean(data: List[float], weights: List[float]) -> float:
    """Weighted mean. Useful when observations have different reliability or frequency."""
    if len(data) != len(weights):
        raise ValueError("data and weights must have the same length")
    total_weight = sum(weights)
    if total_weight == 0:
        raise ValueError("sum of weights must be non-zero")
    return sum(d * w for d, w in zip(data, weights)) / total_weight


def geometric_mean(data: List[float]) -> float:
    """nth root of the product. Appropriate for growth rates and ratios. Requires positive data."""
    if any(d <= 0 for d in data):
        raise ValueError("geometric mean requires strictly positive values")
    log_sum = sum(math.log(d) for d in data)
    return math.exp(log_sum / len(data))


def harmonic_mean(data: List[float]) -> float:
    """n / sum(1/x_i). Appropriate for averaging rates (e.g., speed over equal distances)."""
    if any(d == 0 for d in data):
        raise ValueError("harmonic mean is undefined when any value is 0")
    return len(data) / sum(1 / d for d in data)


def trimmed_mean(data: List[float], proportion: float = 0.1) -> float:
    """Mean computed after discarding the top and bottom `proportion` of values. Robust to outliers."""
    if not 0 <= proportion < 0.5:
        raise ValueError("proportion must be in [0, 0.5)")
    sorted_data = sorted(data)
    k = int(len(sorted_data) * proportion)
    trimmed = sorted_data[k : len(sorted_data) - k] if k > 0 else sorted_data
    return sum(trimmed) / len(trimmed)


def midrange(data: List[float]) -> float:
    """Average of the minimum and maximum. Very sensitive to outliers."""
    return (min(data) + max(data)) / 2
