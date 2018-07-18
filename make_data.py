__author__ = 'andrewlaird'

import numpy as np
import random


def make_test_data(n_rows):


    names = ['Student {}'.format(id_num) for id_num in range(1, n_rows+5)]
    ages = [random.randint(5, 9) for _ in range(1, n_rows+1)]

    return list(zip(names, ages))