import numpy as np
from qq_plot import generate_qq_plot

# Example usage
data = np.random.normal(loc=0, scale=1, size=1000)
generate_qq_plot(data)
