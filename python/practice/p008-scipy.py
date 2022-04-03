#! /usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.linspace(0, 10, 11)
y = np.sin(x)

interpolate.griddata(points,values,xi,method='linear')