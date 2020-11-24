import numpy as np


def estimate_length(*args, **kwargs):
    N_list = kwargs.get('N_list')
    samples_count = kwargs.get('samples_count')
    variance = kwargs.get('variance')
    gamma = kwargs.get('gamma')
    lower = kwargs.get('lower')
    upper = kwargs.get('upper')

    interval_length = np.array([])

    for n in N_list:
        current_length = np.array([])

        for samples_number in range(samples_count):
            sample = np.random.normal(loc=0, scale=variance, size=n)
            l = lower(sample, gamma)
            u = upper(sample, gamma)
            current_length = np.append(current_length, u - l)

        average_length = np.average(current_length)
        interval_length = np.append(interval_length, average_length)

    return interval_length
