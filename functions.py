def booth_function(X, Y):
    """
    Computes the Booth function value for given X and Y values.

    :param X: numpy array of X values.
    :param Y: numpy array of Y values.
    :return: Computed Z values for the function.
    """
    return (X + 2 * Y) ** 2 + (2 * X + Y - 5) ** 2