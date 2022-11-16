#! /usr/bin/python3

import pandas as pd

# pandas.merge函数实现数据表的合并
# API reference
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

# 一对一合并
left = pd.DataFrame({
    'sno': [11, 12, 13, 14],
    'name': ['name_a', 'name_b', 'name_c', 'name_d']
})

right = pd.DataFrame({
    'sno': [11, 12, 13, 14],
    'age': ['21', '22', '23', '24']
})

pd.merge(left, right, on='sno')

# 一对多合并
left = pd.DataFrame({
    'sno': [11, 12, 13, 14],
    'name': ['name_a', 'name_b', 'name_c', 'name_d']
})

right = pd.DataFrame({
    'sno': [11, 11, 11, 12, 15],
    'grade': ['语文88', '英语90', '数学90', '英语75', '数学55']
})

pd.merge(left, right, on='sno')

# 多对多关系
left = pd.DataFrame({
    'sno': [11, 11, 12, 12, 12],
    '爱好': ['篮球', '羽毛球', '乒乓球', '篮球', "足球"]
})

right = pd.DataFrame({
    'sno': [11, 11, 11, 12, 12, 13],
    'grade': ['语文88', '数学90', '英语75', '语文66', '数学55', '英语29']
})

pd.merge(left, right, on='sno')

# 使用index做合并

left.set_index('sno', drop=False, inplace=True)
right.set_index('sno', drop=False, inplace=True)

right.index.names = ['snoindex']
right.rename(columns={'sno': 'sno_right'}, inplace=True)

left
right

pd.merge(left, right, left_index=True, right_index=True)
pd.merge(left, right, left_index=True, right_on='sno_right')

# 理解left join、right join、inner join、outer join的区别

left = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

right = pd.DataFrame({
    'key': ['K0', 'K1', 'K4', 'K5'],
    'C': ['C0', 'C1', 'C4', 'C5'],
    'D': ['D0', 'D1', 'D4', 'D5']
})

left
right

pd.merge(left, right, how='inner', on='key')
pd.merge(left, right, how='left', on='key')
pd.merge(left, right, how='right', on='key')
pd.merge(left, right, how='outer', on='key')

# 如果出现非Key的字段重名怎么办
left = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

right = pd.DataFrame({
    'key': ['K0', 'K1', 'K4', 'K5'],
    'A': ['A10', 'A11', 'A12', 'A13'],
    'D': ['D0', 'D1', 'D4', 'D5']
})

left
right

pd.merge(left, right, on='key')
pd.merge(left, right, on='key', suffixes=('_left', '_right'))

# 包含
left = pd.DataFrame({'pos': ['sd1', 'sd2', 'sd3', 'sd4'], 'val': [0, 0, 0, 0]})

left
left.set_index('pos')

right = pd.DataFrame({'pos': ['sd2', 'sd3', 'sd5'], 'val': [1, 3, 4]})
right.set_index('pos')

m = pd.merge(left, right,  rihgt_index=True, how='outer',
             suffixes=('x', 'y'))

m.fillna({"valy": 0}, inplace=True)
m
