__author__ = 'andrewlaird'

import math


def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

print(sum([nCr(15, class_size) for class_size in range(1, 10)]))