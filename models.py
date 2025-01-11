import numpy as np
import pandas as pd


def least_squares_linear_regression(X, y):
    """
    Computes the parameters for Linear Regression using the Least Squares Estimation (LSE) method.
        the function can handle df/numpy array shape and x can be single input or multi-dimensional.
    :param X: DataFrame or numpy array of shape (n_samples, n_features), the input features.
    :param y: DataFrame or numpy array of shape (n_samples, 1), the target variable.
    :return: numpy array of shape (n_features + 1,), the estimated coefficients including intercept.
    """
    # Convert DataFrame to numpy array if necessary
    if isinstance(X, pd.DataFrame):
        X = X.values
    if isinstance(y, pd.DataFrame):
        y = y.values.ravel() # Convert to 1D numpy array

    # Add intercept term (column of ones) to X
    X = np.c_[np.ones(X.shape[0]), X]

    # Compute the least squares solution: beta = (X^T * X)^(-1) * X^T * y
    beta = np.linalg.pinv(X.T @ X) @ X.T @ y


    return beta

