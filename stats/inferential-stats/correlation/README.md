# Correlation

Correlation measures the strength and direction of association between two variables. Values lie in `[-1, 1]`; the sign indicates direction and the magnitude indicates strength.

## Concepts

- **Pearson's r** — linear correlation. Sensitive to outliers and assumes roughly linear, normal-ish data.
- **Spearman's rho** — Pearson's r applied to *ranks*. Captures monotonic relationships, linear or not.
- **Kendall's tau** — based on the proportion of concordant vs discordant pairs. More conservative than Spearman; preferred for small samples.
- **Covariance** — unscaled version of correlation. Same sign, units of `x * y`.
- **Correlation matrix** — pairwise correlations between many variables. Diagonal is always 1.

Correlation is not causation. Two variables can be strongly correlated through a third confounding variable, by coincidence in small samples, or because one causes the other.

## Files

- `correlation.py` — `pearson`, `spearman`, `kendall`, `covariance_matrix`, `correlation_matrix`.
- `main.py` — examples on linear, non-linear monotonic, and uncorrelated data.

## Usage

```bash
python stats/inferential-stats/correlation/main.py
```
