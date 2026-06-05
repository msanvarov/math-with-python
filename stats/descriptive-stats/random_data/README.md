# Random Data Generation

Generating synthetic data from known distributions is useful for testing statistical methods, prototyping plots, and building intuition for distributional shapes.

## Distributions covered

| Distribution | Models | Parameters |
| --- | --- | --- |
| Uniform | Equally likely outcomes on an interval | `low`, `high` |
| Normal | Symmetric bell-curve data | `mean`, `std` |
| Exponential | Time between events in a Poisson process | `scale` (mean) |
| Binomial | Successes in `n` independent Bernoulli trials | `n`, `p` |
| Poisson | Counts of events at a fixed rate | `lam` |
| Lognormal | Positive, right-skewed data (incomes, asset returns) | `mean`, `sigma` of the underlying normal |
| Beta | Probabilities and proportions on `[0, 1]` | `alpha`, `beta` |

Every function accepts an optional `seed` for reproducibility.

## Files

- `random_data_generator.py` — wrappers around `numpy.random.default_rng` for each distribution.
- `main.py` — draws 1,000 samples from each distribution and prints summary statistics.

## Usage

```bash
python stats/descriptive-stats/random_data/main.py
```

Pair with the [QQ plots](../qq_plots/README.md) module to visually verify how well a sample matches a theoretical distribution.
