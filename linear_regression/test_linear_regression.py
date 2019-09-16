### Test file for linear_regression ###

import numpy as np
from linear_regression import *


def test_simulate_data():
    """
    Ensures that the simulate_data method returns data.

    """
    try:
        data = simulate_data()
    except:
        raise Warning("Failed to compute simulated data.")


def test_compare_models():
    """
    Test compare_models function.

    """
    data = simulate_data()
    X = data['X']
    y = data['y']
    beta = data['beta']

    results = compare_models(X, y, beta)

    # statsmodels is accurate
    assert np.linalg.norm(results['statsmodels']-results['truth']) < .5

    # sklearn is accurate
    assert np.linalg.norm(results['sklearn']-results['truth']) < .5

    # sklearn method == statsmodels method
    assert np.allclose(results['sklearn'], results['statsmodels'])


def test_load_hospital_data():
    """
    Test load_hospital_data function.

    """
    try:
        df = load_hospital_data("./hospital_charge_sample.csv")
    except:
        raise ValueError("Unable to load dataset")


def test_prepare_data():
    """
    Test prepare_data function.

    """
    try:
        df = load_hospital_data("./hospital_charge_sample.csv")
        data = prepare_data(df)
    except:
        raise ValueError("Method 'prepare_data' failed")


def test_run_hospital_regression():
    """
    Test run_hospital_regression function.
    
    """
    results = run_hospital_regression("./hospital_charge_sample.csv")

    assert type(results) == str


# Tests on simulated data sets
data = test_simulate_data()
test_compare_models()
test_run_hospital_regression()


### END ###
