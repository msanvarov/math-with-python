To generate QQ plots in Python, we can use the `statsmodels` library. QQ plots are used to compare the quantiles of a dataset against the quantiles of a theoretical distribution, typically the normal distribution. This allows us to visually assess if the dataset follows a particular distribution.

To create QQ plots, we need to follow these steps:

1. Import the necessary libraries.
2. Generate a random dataset or load an existing dataset.
3. Fit a theoretical distribution to the dataset.
4. Calculate the quantiles of the dataset and the theoretical distribution.
5. Plot the quantiles on a scatter plot.

Let's start by creating the entrypoint file `qq_plot.py`
