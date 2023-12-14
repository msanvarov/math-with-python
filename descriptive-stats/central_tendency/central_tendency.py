from typing import List
from collections import Counter

def compute_mean(data: List[float]) -> float:
    """
    Compute the mean of a list of numbers.

    Args:
        data (List[float]): The list of numbers.

    Returns:
        float: The mean of the numbers.
    """
    return sum(data) / len(data)

def compute_median(data: List[float]) -> float:
    """
    Compute the median of a list of numbers.

    Args:
        data (List[float]): The list of numbers.

    Returns:
        float: The median of the numbers.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]

def compute_mode(data: List[float]) -> List[float]:
    """
    Compute the mode(s) of a list of numbers.

    Args:
        data (List[float]): The list of numbers.

    Returns:
        List[float]: The mode(s) of the numbers.
    """
    counter = Counter(data)
    max_count = max(counter.values())
    modes = [num for num, count in counter.items() if count == max_count]
    return modes
