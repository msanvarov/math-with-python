"""Common hypothesis tests built on scipy.stats."""

from dataclasses import dataclass

import numpy as np
from scipy import stats


@dataclass
class TestResult:
    statistic: float
    p_value: float
    reject_null: bool

    def __str__(self):
        verdict = "reject H0" if self.reject_null else "fail to reject H0"
        return f"statistic={self.statistic:.4f}, p={self.p_value:.4g} -> {verdict}"


def one_sample_t_test(data, popmean, alpha=0.05):
    """Is the sample mean different from a known population mean?"""
    t, p = stats.ttest_1samp(data, popmean)
    return TestResult(float(t), float(p), p < alpha)


def two_sample_t_test(a, b, alpha=0.05, equal_var=False):
    """Welch's t-test (equal_var=False) compares means of two independent samples."""
    t, p = stats.ttest_ind(a, b, equal_var=equal_var)
    return TestResult(float(t), float(p), p < alpha)


def paired_t_test(before, after, alpha=0.05):
    """Are paired observations (e.g., before/after) different on average?"""
    t, p = stats.ttest_rel(before, after)
    return TestResult(float(t), float(p), p < alpha)


def chi_square_independence(contingency_table, alpha=0.05):
    """Chi-square test of independence on a contingency table."""
    chi2, p, dof, expected = stats.chi2_contingency(np.asarray(contingency_table))
    return TestResult(float(chi2), float(p), p < alpha)


def shapiro_wilk(data, alpha=0.05):
    """Test for normality. H0: data is drawn from a normal distribution."""
    w, p = stats.shapiro(data)
    return TestResult(float(w), float(p), p < alpha)


def mann_whitney_u(a, b, alpha=0.05):
    """Non-parametric alternative to the two-sample t-test."""
    u, p = stats.mannwhitneyu(a, b, alternative="two-sided")
    return TestResult(float(u), float(p), p < alpha)
