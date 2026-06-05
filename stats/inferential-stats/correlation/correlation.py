"""Correlation measures for paired data."""

import numpy as np
from scipy import stats


def pearson(x, y):
    """Pearson's r: linear correlation, in [-1, 1]. Returns (r, p_value)."""
    r, p = stats.pearsonr(x, y)
    return float(r), float(p)


def spearman(x, y):
    """Spearman's rho: rank-based correlation, robust to monotonic but non-linear relationships."""
    rho, p = stats.spearmanr(x, y)
    return float(rho), float(p)


def kendall(x, y):
    """Kendall's tau: rank correlation based on concordant vs discordant pairs."""
    tau, p = stats.kendalltau(x, y)
    return float(tau), float(p)


def covariance_matrix(*samples):
    """Sample covariance matrix of one or more variables."""
    return np.cov(np.vstack(samples))


def correlation_matrix(*samples):
    """Pearson correlation matrix."""
    return np.corrcoef(np.vstack(samples))
