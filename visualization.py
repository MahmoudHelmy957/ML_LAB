#TODO: make 2d visualization of any function
#TODO: make 3d visualization of any function
import matplotlib.pyplot as plt
import numpy as np
from functions import *



def plot_3d_function(equation, x_range=(-15, 15), y_range=(-15, 15), reso=42, title="3D Function Plot"):
    """
    Plots a 3D function given an equation function.

    :param equation: A function representing the equation f(X, Y) -> Z.
    :param x_range: Tuple (min, max) defining the range for X-axis.
    :param y_range: Tuple (min, max) defining the range for Y-axis.
    :param reso: Resolution for the mesh grid.
    :param title: Title of the plot.
    """
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(6, 6))

    X = np.linspace(x_range[0], x_range[1], reso)
    Y = np.linspace(y_range[0], y_range[1], reso)
    X, Y = np.meshgrid(X, Y)
    Z = equation(X, Y)

    surf = ax.plot_surface(X, Y, Z, cmap='jet_r', linewidth=0, antialiased=True)

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    plt.title(title)

    plt.show()