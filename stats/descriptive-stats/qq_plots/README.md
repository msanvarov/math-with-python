# QQ Plots

A quantile-quantile (QQ) plot compares the quantiles of a dataset against the quantiles of a theoretical distribution. If the points fall close to the 45-degree reference line, the dataset is well approximated by that distribution.

## Concepts

- **Quantile** — a cut point that divides the data into intervals of equal probability.
- **Reference line** — the 45-degree line representing a perfect match between observed and theoretical quantiles.
- **Heavy tails / skew** — systematic deviation from the reference line at the ends of the plot indicates tail behavior or skew not captured by the chosen distribution.

## How to read a QQ plot

1. Generate or load a dataset.
2. Pick a theoretical distribution (normal by default).
3. Plot the sample quantiles against the theoretical quantiles.
4. Compare the resulting curve to the 45-degree line.

## Files

- `qq_plot.py` — `generate_qq_plot(data, dist='norm')`, built on `statsmodels.ProbPlot` and `scipy.stats`.
- `main.py` — example usage on 1,000 samples drawn from a standard normal.

## Usage

```bash
python stats/descriptive-stats/qq_plots/main.py
```
