### Tools for linear regression ###

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm


def simulate_data(nobs=1000):
    """
    Simulates data for testing linear_regression models.
    INPUT
        nobs (int) the number of observations in the dataset

    RETURNS
        data (dict) contains X, y, and beta vectors.

    """

    x0 = np.ones(nobs)
    x1 = np.random.normal(5000, 500000, size=nobs)
    x2 = np.random.poisson(15, size=nobs)
    X = np.column_stack((x0, x1, x2))

    beta = np.random.normal(0,2.5,size=X.shape[1])
    epsilon = np.random.randn(nobs)

    y = X.dot(beta) + epsilon

    data = dict()
    data['X'] = X
    data['y'] = y
    data['beta'] = beta

    return data


def compare_models(X, y, beta=None):
    """
    Compares output from different implementations of OLS.
    INPUT
        X (ndarray) the independent variables in matrix form
        y (array) the response variables vector

    RETURNS
        results (pandas.DataFrame) of estimated beta coefficients

    """

    # Using statsmodels OLS
    output_sm = sm.OLS(y, X).fit()
    beta_sm = output_sm.params

    # Using sklearn's Linear Regression
    output_skl = LinearRegression(fit_intercept=False).fit(X, y)
    beta_skl = output_skl.coef_

    results = pd.DataFrame()
    results['statsmodels'] = beta_sm
    results['sklearn'] = beta_skl

    if beta is not None:
        results['truth'] = beta

    return results


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


def prepare_data(df):
    """
    Prepares hospital data for regression (basically turns df into X and y).
    INPUT
        df (pandas.DataFrame) the hospital dataset

    RETURNS
        data (dict) containing X design matrix and y response variable

    """
    data = dict()

    X1 = np.log(df['total discharges'].values)
    X2 = np.log(df['average covered charges'].values)
    X = np.column_stack((np.ones(len(X1)), X1, X2))

    Y = np.log(df['average total payments'].values)

    data['X'] = X
    data['y'] = Y

    return data


def run_hospital_regression(path_to_data):
    """
    Loads hospital charge data and runs OLS on it.
    INPUT
        path_to_data (str) filepath of the csv file

    RETURNS
        results (str) the statsmodels regression output

    """
    df = load_hospital_data(path_to_data)
    data = prepare_data(df)
    results = sm.OLS(data['y'], data['X']).fit().summary().as_text()

    return results
 

### END ###
