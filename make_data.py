__author__ = 'andrewlaird'

import numpy as np
import random


def make_test_data(n_rows):

    names = ['Student {}'.format(id_num) for id_num in range(1, n_rows+1)]
    ages = [random.randint(6, 14) for _ in range(1, n_rows+1)]
    reading_levels = [round(np.random.normal(age, 1.5)) for age in ages]

    return list(zip(names, ages, reading_levels))