# Central Tendency

Measures of central tendency summarize a dataset with a single representative value.

## Concepts

- **Mean (arithmetic)** — the average. Sensitive to outliers.
- **Median** — the middle of sorted data. Robust to outliers; preferred for skewed distributions.
- **Mode** — the most common value(s). The only measure that works on categorical data.
- **Weighted mean** — observations contribute proportionally to their weight. Used for grade averages, importance-weighted scores.
- **Geometric mean** — `n`th root of the product. Right for ratios and growth rates because it averages multiplicative effects.
- **Harmonic mean** — `n / sum(1/x_i)`. Right for averaging rates (e.g., speed over equal distances).
- **Trimmed mean** — discard the top and bottom `p%` before averaging. Robust to outliers without throwing away as much information as the median.
- **Midrange** — `(min + max) / 2`. Maximally sensitive to outliers.

## Files

- `central_tendency.py` — all measures listed above, implemented in pure Python.
- `main.py` — examples including weighted grade averages, geometric growth, and how trimming handles outliers.

## Usage

```bash
python stats/descriptive-stats/central_tendency/main.py
```
