import numpy as np
import matplotlib.pyplot as plt
from parameter_estimation import get_errors


def plot_unif(size, samples_count, moments, theta):
    plt.title("Mean squared error for $\\theta$ in $U[0; \\theta]$")
    plt.xlabel("Moment")
    plt.ylabel("Mean squared error")
    y = get_errors(size, samples_count, moments, "unif", theta)
    plt.grid(True)
    plt.plot(moments, y)
    plt.show()


def plot_unif_log(size, samples_count, moments, theta):
    plt.title("Log of mean squared error for $\\theta$ in $U[0; \\theta]$")
    plt.xlabel("Moment")
    plt.ylabel("Log mean squared error")
    y = get_errors(size, samples_count, moments, "unif", theta)
    plt.grid(True)
    plt.plot(moments, np.log(y))
    plt.show()


def plot_exp(size, samples_count, moments, theta):
    plt.title("Mean squared error for $\\theta$ in $Exp(\\theta)$")
    plt.xlabel("Moment")
    plt.ylabel("Mean squared error")
    y = get_errors(size, samples_count, moments, "exp", theta)
    plt.grid(True)
    plt.plot(moments, y)
    plt.show()

