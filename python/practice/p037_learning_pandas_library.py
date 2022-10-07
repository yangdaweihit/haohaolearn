#! /usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd

# --------------- Series ---------------

songs2 = pd.Series([145, 142, 38, 13], name='Counts')

# Series属性
songs2.index  # 此时类型为 integer
songs2.values
songs2.name

# 用字符串列表作为index
songs2 = pd.Series([145, 142, 38, 13],
                   name='Counts',
                   index=['Paul', 'John', 'George', 'Ringo'])

songs2.index  # 此时类型为 object
songs2.values
songs2.name

mask = songs2 > songs2.median()

mask
songs2[mask]

# --------------- Series CRUD ---------------

# The previous example illustrates an interesting feature of pandas—the
# index values are strings and they are not unique. This can cause some
# confusion, but can also be useful when duplicate index items are needed.

# Creation
george_dupe = pd.Series([10, 7, 1, 22],
                        index=['1968', '1969', '1970', '1970'],
                        name='George Songs')
george_dupe['1970']

s = {'a': 0, 'b': 1, 'c': 2}
t = pd.Series(s)

22 in set(george_dupe)
22 in george_dupe.values

# iteration is over the values of the series
# membership is over the index names
'1970' in george_dupe

# To iterate over the tuples containing both the index label and the value, use the .iteritems method

for item in george_dupe.iteritems():
    print(item)

# Updating
george_dupe['1969'] = 6
george_dupe['1973'] = 11
george_dupe['1970'] = 1970
george_dupe.iloc[3] = 22
george_dupe

# Deletion
del george_dupe['1973']

# To delete values from a series, it is more common to filter the
# series to get a new series.

george_dupe
george_dupe[george_dupe <= 10]

# Series Indexing

george = pd.Series([10, 2, 7],
                   index=['1968', '1970', '1969'],
                   name='George Songs')
george.index

george
george[0]
george[-1]

george['1970']
george.iloc[1]
george.loc['1970']
george.at['1970']
george.iat[1]

george.iloc[:2]
george.iloc[-2:]

mask = george >= 7
george[mask]

# --------------- Series Methods ---------------

songs_66 = pd.Series([3, None, 11, 9],
                     index=['George', 'Ringo', 'John', 'Paul'],
                     name='Counts')
songs_69 = pd.Series([18, 22, 7, 5],
                     index=['John', 'Paul', 'George', 'Ringo'],
                     name='Counts')
# Iteration
for value in songs_66:
    print(value)

for idx, value in songs_66.iteritems():
    print(idx, value)

for idx in songs_66.keys():
    print(idx)

# Overloaded operations
songs_66 + songs_69
songs_66.fillna(0) + songs_69.fillna(0)

# Getting and Setting Values

# --------------- DataFrames ---------------

# --------------- DataFrames Example ---------------
