# Hypothesis Testing

Hypothesis tests quantify how surprising the observed data would be if a default assumption (the *null hypothesis* `H0`) were true. A small p-value means "this data would be unusual under `H0`", which we treat as evidence against it.

## Concepts

- **Null vs alternative hypothesis** — `H0` is the boring default, `H1` is the effect we want to detect.
- **Test statistic** — a single number summarizing the data (e.g., the t-statistic).
- **p-value** — the probability of seeing a test statistic at least as extreme as the observed one, assuming `H0` is true.
- **Significance level alpha** — the threshold (commonly 0.05) below which we reject `H0`.
- **Type I error** — rejecting a true `H0` (false positive). Type II is failing to reject a false `H0` (false negative).
- **Parametric vs non-parametric** — parametric tests (t-test) assume a distribution; non-parametric tests (Mann-Whitney) don't.

## Tests included

| Test | When to use |
| --- | --- |
| One-sample t-test | Is the sample mean different from a known value? |
| Two-sample (Welch) t-test | Do two independent groups have different means? |
| Paired t-test | Did paired observations (before/after) change? |
| Chi-square independence | Are two categorical variables associated? |
| Shapiro-Wilk | Is the data normally distributed? |
| Mann-Whitney U | Non-parametric alternative to the two-sample t-test. |

## Files

- `hypothesis_testing.py` — thin wrappers around `scipy.stats` that return a `TestResult` dataclass with a built-in verdict at the chosen alpha.
- `main.py` — runs each test on simulated data.

## Usage

```bash
python stats/inferential-stats/hypothesis_testing/main.py
```
