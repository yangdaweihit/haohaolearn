#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Numpy手册
# Routines > Input and output
# https://docs.scipy.org/doc/numpy/reference/routines.io.html

import numpy as np
from io import StringIO

if __name__ == '__main__':

    c = StringIO(u"0 1\n2 3")
    np.loadtxt(c)

    # loadtxt
    # unpack为真时，返回的数组被转置。将各列赋予各域。
    x, y = np.loadtxt("data.txt",
                      delimiter=",",
                      unpack=True,
                      usecols=(0, 2),
                      skiprows=2)

    # savetxt
    # x第一行， y第二行
    np.savetxt("data.out", (x, y),
               fmt='%5.2f',
               header='****************',
               footer='================',
               delimiter=" ")

    # genfromtxt
    a, b = np.genfromtxt("data.txt",
                         delimiter=",",
                         unpack=True,
                         usecols=(0, 1))
