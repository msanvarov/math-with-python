# Dispersion

Measures of dispersion describe how spread out a dataset is around its center.

## Concepts

- **Range** — `max - min`. Simple but very sensitive to outliers.
- **Variance** — average squared deviation from the mean. Reported in squared units. Population divides by `n`; sample divides by `n - 1`.
- **Standard deviation** — square root of the variance, in the original units.
- **Coefficient of variation (CV)** — `std / mean`, as a percentage. Lets you compare variability across datasets with different scales or units.
- **Mean absolute deviation (MAD)** — average absolute distance from the mean. Less inflated by outliers than variance.
- **Median absolute deviation** — median of absolute deviations from the median. The robust alternative to standard deviation.
- **Percentile** — value below which a given percent of the data falls.
- **Z-scores** — standardized values `(x - mean) / std`. Express each observation as "this many standard deviations from the mean."

## Files

- `dispersion.py` — all of the above. `calculate_variance`/`_standard_deviation` accept a `sample=True` flag for the unbiased estimator.
- `main.py` — examples including z-scores and several percentiles.

## Usage

```bash
python stats/descriptive-stats/dispersion/main.py
```
