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
    Compares output from different implementations of OLS.
    INPUT
        X (ndarray) the independent variables in matrix form
        y (array) the response variables vector

    RETURNS
        results (pandas.DataFrame) of estimated beta coefficients

    """

    # Compute OLS
    beta_ols = OLS(X, y)

    # Using statsmodels OLS
    output_sm = sm.OLS(y, X).fit()
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
        beta (array) the estimated model coefficients

    """
    df = load_hospital_data(path_to_data)
    data = prepare_data(df)
    beta = OLS(data['X'], data['y'])

    return beta
 



### END ###
