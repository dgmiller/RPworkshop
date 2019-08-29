### Test file for linear_regression ###
import numpy as np
from linear_regression import *


def test_simulate_data():
    try:
        data = simulate_data()
        return data
    except:
        raise Warning("Failed to compute simulated data.")


def test_OLS(data):
    """
    test 1 on simulated data
    test 2 on actual data set
    """
    X = data['X']
    y = data['y']
    beta = data['beta']

    beta_est = OLS(X, y)
    error = beta - beta_est
    for err in error:
        assert abs(err) < .05


def test_compare_models(data):
    """
    test 1 on simulated data
    test 2 on actual data set
    """
    X = data['X']
    y = data['y']
    beta = data['beta']

    results = compare_models(X, y)
    results['truth'] = beta

    print(results)


# Tests on simulated data sets
data = test_simulate_data()
test_OLS(data)
test_compare_models(data)

### END ###
