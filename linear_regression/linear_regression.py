### Tools for linear regression ###

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm


def OLS(X,y):
    """
    Estimates beta coefficients using ordinary least squares.
    INPUT
        X (ndarray) the matrix representing the independent variables.
        y (array) the vector representing the response variable.

    RETURNS
        beta_est (array) the estimated coefficients for the least squares problem.

    """
    XpXi = np.linalg.inv(X.T.dot(X))
    XpY = X.T.dot(y)
    beta_est = XpXi.dot(XpY)
    return beta_est


def compare_models(X, y):
    """
    """

    # Compute OLS
    beta_ols = OLS(X, y)

    # Using statsmodels OLS
    output_sm = sm.OLS(y,X).fit()
    beta_sm = output_sm.params

    # Using sklearn's Linear Regression
    output_skl = LinearRegression().fit(X, y)
    beta_skl = output_skl.coef_

    results = pd.DataFrame()
    results['OLS'] = beta_ols
    results['statsmodels'] = beta_sm
    results['sklearn'] = beta_skl

    return results


def simulate_data():
    """
    Simulates data for testing linear_regression models.
    RETURNS
        data (dict) contains X, y, and beta vectors.

    """
    beta = np.random.normal(0,2.5,size=10)
    epsilon = np.random.randn(100)

    X = np.random.normal(22,5,size=1000).reshape((100,10))
    y = X.dot(beta) + epsilon

    data = dict()
    data['X'] = X
    data['y'] = y
    data['beta'] = beta

    return data


def load_hospital_data(path_to_data):
    """
    Loads the hospital charges data set found at data.gov.
    INPUT
        path_to_data (str) indicates the filepath to the hospital charge data (csv)

    RETURNS
        df (pandas.DataFrame) containing the cleaned and formatted dataset for regression

    """

    # load csv with pandas
    df = pd.read_csv(path_to_data)

    # rename/reformat the columns
    rename_dict = dict()
    for c in df.columns:
        rename_dict[c] = c.lower().strip()
    df = df.rename(columns=rename_dict)

    # begin transforming variables for regression
    # drop unwanted variables
    vars_to_drop = ['hospital referral region description',
                    'provider street address',
                    'provider name',
                    'provider city',
                    'provider state']
    df = df.drop(vars_to_drop, axis=1)

    return df



### END ###
