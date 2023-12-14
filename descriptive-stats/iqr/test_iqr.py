import pytest
from iqr import IQR

def test_iqr():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    iqr_calculator = IQR(data)
    assert iqr_calculator.calculate_iqr() == 4.5

if __name__ == "__main__":
    pytest.main()
