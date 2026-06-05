import numpy as np

from random_data_generator import (
    generate_uniform_data,
    generate_normal_data,
    generate_exponential_data,
    generate_binomial_data,
    generate_poisson_data,
    generate_lognormal_data,
    generate_beta_data,
)

SIZE = 1000
SEED = 0


def summarize(name, sample):
    print(f"{name}: mean={sample.mean():.3f}, std={sample.std():.3f}, "
          f"min={sample.min():.3f}, max={sample.max():.3f}")


summarize("uniform(0, 10)", generate_uniform_data(SIZE, low=0, high=10, seed=SEED))
summarize("normal(0, 1)", generate_normal_data(SIZE, seed=SEED))
summarize("exponential(scale=2)", generate_exponential_data(SIZE, scale=2, seed=SEED))
summarize("binomial(n=10, p=0.3)", generate_binomial_data(SIZE, n=10, p=0.3, seed=SEED))
summarize("poisson(lambda=3)", generate_poisson_data(SIZE, lam=3, seed=SEED))
summarize("lognormal(mean=0, sigma=1)", generate_lognormal_data(SIZE, seed=SEED))
summarize("beta(alpha=2, beta=5)", generate_beta_data(SIZE, alpha=2, beta=5, seed=SEED))
