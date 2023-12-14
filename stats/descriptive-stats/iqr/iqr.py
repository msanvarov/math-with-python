import numpy as np

class IQR:
    def __init__(self, data):
        self.data = data

    def calculate_iqr(self):
        q1 = np.percentile(self.data, 25)
        q3 = np.percentile(self.data, 75)
        iqr = q3 - q1
        return iqr

    def print_iqr(self):
        iqr = self.calculate_iqr()
        print(f"The interquartile range is: {iqr}")
