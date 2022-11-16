#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://docs.python.org/3/library/time.html

- UTC: Coordinated Universal Time (formerly known as Greenwich Mean
Time, or GMT)，世界标准时间，正式名称为：格林威治标准时间。

"""


import time

time.gmtime(time.time())
time.localtime(time.time())

time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
