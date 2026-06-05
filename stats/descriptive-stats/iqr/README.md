# Interquartile Range (IQR)

The interquartile range is the spread of the middle 50% of a dataset, defined as `Q3 - Q1` (the difference between the 75th and 25th percentiles). It is a robust measure of dispersion that ignores extreme values, which makes it useful for skewed distributions and outlier detection.

## Concepts

- **Q1** — 25th percentile.
- **Q3** — 75th percentile.
- **IQR** — `Q3 - Q1`.
- **Outlier rule of thumb** — values outside `[Q1 - 1.5 * IQR, Q3 + 1.5 * IQR]` are commonly flagged as outliers.

## Files

- `iqr.py` — the `IQR` class wraps a dataset and computes the IQR using `numpy.percentile`.
- `main.py` — example usage.
- `test_iqr.py` — `pytest` test verifying the IQR of `[1..10]` is `4.5`.

## Usage

```bash
python stats/descriptive-stats/iqr/main.py
pytest stats/descriptive-stats/iqr/test_iqr.py
```
