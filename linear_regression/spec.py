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


def test_OLS():
    """
    Ensures that the estimated betas are within .05 of the true betas.

    """
    data = simulate_data()
    X = data['X']
    y = data['y']
    beta = data['beta']

    beta_est = OLS(X, y)

    assert np.linalg.norm(beta - beta_est) < .1


def test_compare_models():
    """
    Test compare_models function.

    """
    data = simulate_data()
    X = data['X']
    y = data['y']
    beta = data['beta']

    results = compare_models(X, y)
    results['truth'] = beta

    # OLS is roughly the same as statsmodels OLS
    assert np.linalg.norm(results['OLS']-results['statsmodels']) < .1

    # OLS is roughly the same as sklearn
    assert np.linalg.norm(results['OLS']-results['sklearn']) < .1

    # statsmodels is accurate
    assert np.linalg.norm(results['statsmodels']-results['truth']) < .1

    # sklearn is accurate
    assert np.linalg.norm(results['sklearn']-results['truth']) < .1


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
    beta = run_hospital_regression("./hospital_charge_sample.csv")

    # test against statsmodels implementation
    df = load_hospital_data("./hospital_charge_sample.csv")
    data = prepare_data(df)
    beta_sm = sm.OLS(data['y'], data['X']).fit().params

    assert np.allclose(beta, beta_sm)


# Tests on simulated data sets
data = test_simulate_data()
test_OLS()
test_compare_models()
test_run_hospital_regression()


### END ###
