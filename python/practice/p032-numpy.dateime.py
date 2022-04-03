#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://numpy.org/doc/stable/reference/arrays.datetime.html
"""

import numpy as np

# 日期
np.datetime64('2005-02-25')

# 月份
b = np.datetime64('2005-02')

# 强迫以日期存储
np.datetime64('2005-02', 'D')

np.array(['2007-07-13', '2006-01-13', '2010-08-13'], dtype='datetime64')

np.arange('2005-02', '2005-03', dtype='datetime64[D]')

np.datetime64('2005') == np.datetime64('2005-01-01')

np.timedelta64(1, 'D')
np.timedelta64(4, 'h')

np.datetime64('2009-01-01') - np.datetime64('2008-01-01')

np.datetime64('2009') + np.timedelta64(20, 'D')

np.datetime64('2011-06-15T00:00') + np.timedelta64(12, 'h')

np.timedelta64(1, 'W') / np.timedelta64(1, 'D')

# 定义1年时间段
a = np.timedelta64(1, 'Y')

# 将1年时间段转换为月数，即转换单位
np.timedelta64(a, 'M')
