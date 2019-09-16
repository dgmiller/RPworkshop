#Linear Regression Example

###Objective

Learn how to develop your research using git and GitHub.

###To-Do

In this example, you will implement the following methods in `linear_regression.py` as well as tests for each method in `test_linear_regression.py`:

+ `compare_models()`
+ `simulate_data()`
+ `load_hospital_data()`
+ `prepare_data()`
+ `run_hospital_regression()`

**Let's get started**

The purpose of this exercise is to demonstrate that implementation of the same method (OLS) in two different packages may give slightly different results. Suppose we will be running a regression or a series of regressions on a specific dataset about hospital charge data found online at data.gov/health. There are a number of questions we might want to ask this dataset.

```
                                 OLS Regression Results                                
=======================================================================================
Dep. Variable:                      y   R-squared (uncentered):                   1.000
Model:                            OLS   Adj. R-squared (uncentered):              1.000
Method:                 Least Squares   F-statistic:                          7.712e+04
Date:                Mon, 16 Sep 2019   Prob (F-statistic):                   2.20e-172
Time:                        07:49:31   Log-Likelihood:                         -128.37
No. Observations:                 100   AIC:                                      276.7
Df Residuals:                      90   BIC:                                      302.8
Df Model:                          10                                                  
Covariance Type:            nonrobust                                                  
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
x1            -1.1245      0.019    -60.643      0.000      -1.161      -1.088
x2             2.5044      0.020    123.914      0.000       2.464       2.545
x3             1.6085      0.017     96.915      0.000       1.576       1.642
x4             6.2893      0.018    342.086      0.000       6.253       6.326
x5            -1.5883      0.020    -80.022      0.000      -1.628      -1.549
x6            -5.1080      0.018   -282.434      0.000      -5.144      -5.072
x7             2.7557      0.018    149.065      0.000       2.719       2.792
x8            -3.6592      0.019   -193.913      0.000      -3.697      -3.622
x9             0.5256      0.018     28.674      0.000       0.489       0.562
x10            0.5650      0.017     33.328      0.000       0.531       0.599
==============================================================================
Omnibus:                        1.103   Durbin-Watson:                   2.281
Prob(Omnibus):                  0.576   Jarque-Bera (JB):                0.695
Skew:                          -0.184   Prob(JB):                        0.706
Kurtosis:                       3.179   Cond. No.                         19.0
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```
