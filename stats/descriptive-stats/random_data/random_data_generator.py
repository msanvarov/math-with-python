"""Sample from common probability distributions."""

import numpy as np


def generate_uniform_data(size, low=0, high=1, seed=None):
    """Uniform on [low, high)."""
    rng = np.random.default_rng(seed)
    return rng.uniform(low, high, size)


def generate_normal_data(size, mean=0, std=1, seed=None):
    """Normal (Gaussian) with given mean and standard deviation."""
    rng = np.random.default_rng(seed)
    return rng.normal(mean, std, size)


def generate_exponential_data(size, scale=1, seed=None):
    """Exponential with given scale (mean) parameter."""
    rng = np.random.default_rng(seed)
    return rng.exponential(scale, size)


def generate_binomial_data(size, n=10, p=0.5, seed=None):
    """Number of successes in n independent Bernoulli(p) trials."""
    rng = np.random.default_rng(seed)
    return rng.binomial(n, p, size)


def generate_poisson_data(size, lam=1.0, seed=None):
    """Counts of events occurring at rate `lam` per interval."""
    rng = np.random.default_rng(seed)
    return rng.poisson(lam, size)


def generate_lognormal_data(size, mean=0, sigma=1, seed=None):
    """Lognormal: exp(X) where X is normal. Common for positive, right-skewed data."""
    rng = np.random.default_rng(seed)
    return rng.lognormal(mean, sigma, size)


def generate_beta_data(size, alpha=2, beta=5, seed=None):
    """Beta on [0, 1]. Useful for modeling probabilities and proportions."""
    rng = np.random.default_rng(seed)
    return rng.beta(alpha, beta, size)
