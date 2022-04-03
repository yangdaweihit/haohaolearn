#! /usr/bin/python3
# -*- coding: utf-8 -*-

# SciPy手册
# Interpolation (scipy.interpolate)
# https://docs.scipy.org/doc/scipy/reference/interpolate.html

import numpy as np
from scipy import interpolate

if __name__ == '__main__':

    # scipy.interpolate.interp1d
    a = np.genfromtxt("data.txt", delimiter=",", usecols=(0, 1))
    a1 = a[:, 0]
    a2 = a[:, 1]

    interpolation_function = interpolate.interp1d(a1, a2, kind='linear')
    ai = [1, 1.5, 2.5, 3.5]
    print(interpolation_function(ai))

    # scipy.interpolate.interp2d
    x = [0, 1, 2]
    y = [0, 3]
    z = [[1, 2, 3], [4, 5, 6]]
    f = interpolate.interp2d(x, y, z, kind='linear')
    f(1, 3)
