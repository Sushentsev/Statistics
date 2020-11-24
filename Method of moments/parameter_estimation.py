import numpy as np


def get_error(estimations, param):
    """ Get mean squared error. """
    n = len(estimations)
    return np.sum((estimations - param) ** 2) / n


def get_unif_param(X, k):
    """ Parameter estimation of U[0, theta] using k-th moment. """
    return ((k + 1) * np.average(X ** k)) ** (1 / k)


def get_exp_param(X, k):
    """ Parameter estimation of Exp(theta) using k-th moment. """
    return (np.average(X ** k) / np.math.factorial(k)) ** (1 / k)


def get_errors(size, samples_count, moments, distribution, theta):
    samples = []
    if distribution == "unif":
        samples = np.array([np.random.uniform(0, theta, size) for _ in range(samples_count)])
        get_param = get_unif_param

    if distribution == "exp":
        samples = np.array([np.random.exponential(theta, size) for _ in range(samples_count)])
        get_param = get_exp_param

    errors = []

    for k in moments:
        params = []
        for sample in samples:
            params.append(get_param(sample, k))

        params = np.array(params)
        current_error = get_error(params, theta)
        errors.append(current_error)

    return np.array(errors)
