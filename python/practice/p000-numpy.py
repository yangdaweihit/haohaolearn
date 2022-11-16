#! /usr/bin/python3
# -*- coding: utf-8 -*-

# NumPy中文网
# https://www.numpy.org.cn/

import numpy as np

a = np.arange(15).reshape(3, 5)
a.shape
a.ndim
a.dtype.name
a.itemsize
a.size