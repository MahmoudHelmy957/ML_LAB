#TODO: Gradient descnet of any function
#TODO: Newton method of any function

import numpy as np


def gradient_descent(function, gradient_function, initial_params, learning_rate=0.01, max_iters=1000, tol=1e-6):
    """
    Performs gradient descent to optimize a given function.

    :param function: The function to minimize.
    :param gradient_function: The gradient of the function.
    :param initial_params: Initial values of the parameters (numpy array).
    :param learning_rate: Learning rate (step size).
    :param max_iters: Maximum number of iterations.
    :param tol: Convergence tolerance.
    :return: Optimized parameters and the function value at the optimum.
    """
    params = np.array(initial_params, dtype=float)
    for _ in range(max_iters):
        gradient = np.array(gradient_function(params))
        new_params = params - learning_rate * gradient

        if np.linalg.norm(new_params - params) < tol:
            break

        params = new_params

    return params, function(params)
