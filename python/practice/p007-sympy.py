#! /usr/bin/python3
# -*- coding: utf-8 -*-

# import os
import sys
# import datetime
# import argparse
# from sympy.solvers import solve
from sympy import *

if __name__ == '__main__':

    a, b, c, x = symbols('a b c x')
    # solve(x**3 - 2 * x**2 - 1, x)
    # a = Integral(cos(x) * exp(x), x)
    # Eq(a, a.doit())

    with open("pzq.tex", "w", encoding="UTF-8") as outf:
        s = latex(a * x**2 + b * x + c)
        outf.write(s)
        pass

    [x for x in range(5) if x % 2 == 0]
