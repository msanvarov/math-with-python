import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats

def generate_qq_plot(data, dist='norm'):
    """
    Generate a QQ plot for a given dataset against a theoretical distribution.

    Parameters:
        data (array-like): The dataset to generate the QQ plot for.
        dist (str or scipy.stats distribution instance): The theoretical distribution to compare against.
            Default is 'norm' for the normal distribution.

    Returns:
        None
    """
    # Check if dist is a string and get the corresponding distribution from scipy.stats
    if isinstance(dist, str):
        if dist == 'norm':
            dist = stats.norm
        elif dist == 'ecdf':
            # For ECDF, we don't fit a distribution but use the empirical data directly
            dist = None
        else:
            raise ValueError(f"Unsupported distribution: {dist}")

    # Create a Probability Plot
    if dist:
        pp = sm.ProbPlot(data, dist=dist)
    else:
        pp = sm.ProbPlot(data, dist=stats.norm)

    # Generate QQ plot
    pp.qqplot(line='45')
    plt.title('QQ Plot')
    plt.show()