#! /usr/bin/python3
# -*- coding: utf-8 -*-

# https://github.com/iamseancheney/python_for_data_analysis_2nd_chinese_version/blob/master/%E7%AC%AC05%E7%AB%A0%20pandas%E5%85%A5%E9%97%A8.md
import numpy as np
import pandas as pd
import pandas_datareader.data as web
from numpy import nan as NA

# https://blog.csdn.net/qq_19528953/article/details/79348929
# https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
#

# 5.1 pandas的数据结构介绍

# 初始化空的系列
s = pd.Series()
print(s)

# 用列表初始化系列
obj = pd.Series([4, 7, -5, 3])
obj

# 系列有两个属性：index和values
obj.index
obj.values

# 对各数据点做标记，赋值index
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2.index
obj2.values
obj2[['a', 'd']]
obj2[['a', 'd']] = [1, 2]

obj2
obj2[obj2 > 0]
obj2 * 2

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index=[100, 101, 102, 103])
print(s)
data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
print(s)
df = pd.DataFrame()
print(df)
df = [1, 2, 3, 4, 5]
print(df)
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]

obj = pd.Series([4, 7, -5, 3])
obj.values
obj.index

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2
obj2['a']
obj2['d'] = 6
obj2
obj2[obj2 > 0]
obj2 * 2
obj2
np.exp(obj2)

# 查询索引是否在系列中
'b' in obj2
'e' in obj2

# 用字典初始化系列
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
sdata
obj3 = pd.Series(sdata)
obj3

# 用排好序的列表初始化原来的系列
# 注意：'California'对应的值为NaN，表示Not a Number
# 而原来的Utah因为没有键值对应而被除去
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
obj4

# 数据缺失判断
pd.isnull(obj4)  # 函数
pd.notnull(obj4)
obj4.isnull()  # 实例方法
obj3

# 找出非空的元素
obj4[obj4.notnull().values]

obj4
# 根据运算的索引标签自动对齐数据
obj3 + obj4

# 系列属性，名字，索引名字
obj4.name = 'population'
obj4.index.name = 'state'
obj4

obj
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
obj

# DataFrame
# 用字典初始化数据框
data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
}
frame = pd.DataFrame(data)
len(frame)
frame
frame.head()
# 如果指定了列序列，则DataFrame的列就会按照指定顺序进行排列
pd.DataFrame(data, columns=['year', 'state', 'pop'])

# 如果传入的列在数据中找不到，就会在结果中产生缺失值
frame2 = pd.DataFrame(data,
                      columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five', 'six'])

frame2.columns
frame2

# 通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series
frame2['state']
frame2.state
frame2.year
frame2.loc['three']
frame2['debt'] = 16.5
frame2
frame2['debt'] = np.arange(6.)
frame2
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
val
frame2['debt'] = val
frame2
frame2['eastern'] = frame2.state == 'Ohio'
frame2
# del方法，很不理解
del frame2['eastern']
frame2
frame2.columns
# 定义一个字典
pop = {
    'Nevada': {
        2001: 2.4,
        2002: 2.9
    },
    'Ohio': {
        2000: 1.5,
        2001: 1.7,
        2002: 3.6
    }
}
# 用字典初始化数据框
frame3 = pd.DataFrame(pop)
frame3
# 转置
frame3.T
# 内层字典的键会被合并、排序以形成最终的索引。如果明确指定了索引，则不会这样
pd.DataFrame(pop, index=[2001, 2002, 2003])

# list(range(3))
# list(np.arange(4))
obj = pd.Series(range(3), index=['a', 'b', 'c'])
obj
index = obj.index
# index是一个Index对象 labels对象
index
index[1:]
labels = pd.Index(np.arange(3))
labels
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
obj2
obj2.index is labels

# 5.2 基本功能

# 重新索引 reindex
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj2
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3
# 插值处理
obj3.reindex(range(6), method='ffill')

# 丢弃指定轴上的项
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
new_obj
obj.drop(['d', 'c'])
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
# 用标签序列调用drop会从行标签（axis 0）删除值
data.drop(['Colorado', 'Ohio'])
data.drop('two', axis=1)
data.drop(['two', 'four'], axis='columns')
# 修改obj本身，而不是返回新对象, inplace=True
obj.drop('c', inplace=True)
obj
# 索引、选取和过滤
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
obj
obj['b']
obj[1]
# 利用整数作索引，不含末端
obj[1:2]
# 利用标签的切片运算与普通的Python切片运算不同，其末端是包含的
obj['b':'c']

# 用切片可以对Series的相应部分进行设置
obj['b':'c'] = 5
obj
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
data
# 通过切片或布尔型数组选取数据
data['two']
data[['three', 'one']]
data[:2]
data[data['three'] > 5]

# 通过布尔型DataFrame（比如下面这个由标量比较运算得出的）进行索引
data < 5
data[data < 5] = 0
data
# 用loc和iloc进行选取
# 对于DataFrame的行的标签索引，我引入了特殊的标签运算符loc和iloc
data.loc['Colorado', ['two', 'three']]
data.iloc[2, [3, 0, 1]]
data.loc[:'Utah', 'two']
data.iloc[:, :3][data.three > 5]
# 整数索引
ser = pd.Series(np.arange(3.))
ser
ser[-1]
ser[2]
ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
ser2[-1]
ser2[1]
# 算术运算和数据对齐
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
s1
s2
s1 + s2
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)),
                   columns=list('bcd'),
                   index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                   columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df1
df2
df1 + df2
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})
df1 + df2

# 在算术方法中填充值

# 5.3 汇总和计算描述统计

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])

df
df.sum()
df.sum(axis=1)
df.mean(axis='columns', skipna=False)
# 返回最大值的间接索引
df.idxmax()
# 累计统计
df.cumsum()
df.describe()
obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
obj.describe()

# 相关系数与协方差

all_data = {
    ticker: web.get_data_yahoo(ticker)
    for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']
}

all_data
web.get_data_yahoo('IBM')

# https://github.com/iamseancheney/python_for_data_analysis_2nd_chinese_version/blob/master/%E7%AC%AC07%E7%AB%A0%20%E6%95%B0%E6%8D%AE%E6%B8%85%E6%B4%97%E5%92%8C%E5%87%86%E5%A4%87.md
# 7.1 处理缺失数据

data = pd.Series([1, NA, 3.5, NA, 7])
data
# 等价方式，去除NaN
data.dropna()
data[data.notnull()]
data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
data
# 去掉含有NaN的行
cleaned = data.dropna()
cleaned
# 传入how='all'将只丢弃全为NA的那些行：
data.dropna(how='all')

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
data[4] = NA
data
# 用这种方式丢弃列，只需传入axis=1即可
data.dropna(axis=1, how='all')
df = pd.DataFrame(np.random.randn(7, 3))
df
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
df
df.dropna()
df
df.dropna(thresh=1)
df.dropna(thresh=2)
df.dropna(thresh=3)
df.fillna(0)
# 若是通过一个字典调用fillna，就可以实现对不同的列填充不同的值
df.fillna({1: 0.5, 2: 0})
df
df.fillna(0, inplace=True)
df
df = pd.DataFrame(np.random.randn(6, 3))
df
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
df
df.fillna(method='ffill')
df.fillna(method='ffill', limit=2)
df.fillna(method='ffill', limit=3)
data = pd.Series([1., NA, 3.5, NA, 7])
data
data.fillna(data.mean())
# 7.2 数据转换
# 移除重复数据
data = pd.DataFrame({
    'k1': ['one', 'two'] * 3 + ['two'],
    'k2': [1, 1, 2, 3, 3, 4, 4]
})
data
data.duplicated()
data.drop_duplicates(['k1'])
data.drop_duplicates(['k2'])
data['v1'] = range(7)
data
data.drop_duplicates(['k1'])
data
data.drop_duplicates(['k1', 'k2'])
data.drop_duplicates(['k1', 'k2'], keep='last')
# 利用函数或映射进行数据转换
data = pd.DataFrame({
    'food': [
        'bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon',
        'pastrami', 'honey ham', 'nova lox'
    ],
    'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]
})
data

meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}

lowercased = data['food'].str.lower()
meat_to_animal
lowercased
data
data['animal'] = lowercased.map(meat_to_animal)
data

# 替换值
data = pd.Series([1., -999., 2., -999., -1000., 3.])
data
data.replace(-999, np.nan)
data.replace([-999, -1000], np.nan)
data.replace([-999, -1000], [np.nan, 0])
# 传入是一个字典
data.replace({-999: np.nan, -1000: 0})

# 重命名轴索引
data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

data
transform = lambda x: x[:4].upper()
data.index.map(transform)
data.rename(index=str.title, columns=str.upper)
data
data.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'})

# 离散化和面元划分
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
cats
cats.codes
cats.categories
pd.value_counts(cats)

# https://github.com/iamseancheney/python_for_data_analysis_2nd_chinese_version/blob/master/%E7%AC%AC08%E7%AB%A0%20%E6%95%B0%E6%8D%AE%E8%A7%84%E6%95%B4%EF%BC%9A%E8%81%9A%E5%90%88%E3%80%81%E5%90%88%E5%B9%B6%E5%92%8C%E9%87%8D%E5%A1%91.md

# https://github.com/iamseancheney/python_for_data_analysis_2nd_chinese_version/blob/master/%E7%AC%AC06%E7%AB%A0%20%E6%95%B0%E6%8D%AE%E5%8A%A0%E8%BD%BD%E3%80%81%E5%AD%98%E5%82%A8%E4%B8%8E%E6%96%87%E4%BB%B6%E6%A0%BC%E5%BC%8F.md
df = pd.read_csv("ex1.csv")

df
pd.read_table('ex1.csv', sep=',')
pd.read_csv('ex2.csv', header=None)
pd.read_csv('ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
pd.read_table('ex2.csv', sep=',')
names = ['a', 'b', 'c', 'd', 'message']
pd.read_csv('ex2.csv', names=names, index_col='message')
list(open('ex1.csv'))
result = pd.read_csv('examples/ex5.csv')
result
pd.isnull(result)

df1 = pd.DataFrame({
    'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
    'data1': range(7)
})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})
df1
df2
pd.merge(df1, df2)
pd.merge(df1, df2, on='key')

df3 = pd.DataFrame({
    'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
    'data1': range(7)
})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})

df3
df4
pd.merge(df3, df4, left_on='lkey', right_on='rkey')

lefth = pd.DataFrame({
    'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
    'key2': [2000, 2001, 2002, 2001, 2002],
    'data': np.arange(5.)
})
righth = pd.DataFrame(
    np.arange(12).reshape((6, 2)),
    index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
           [2001, 2000, 2000, 2000, 2001, 2002]],
    columns=['event1', 'event2'])
lefth
righth

mydct = {'temp_c': [17.0, 25.0], 't': [1, 2]}
df = pd.DataFrame(mydct, index=['Portland', 'Berkeley'])
df
df.assign(temp_f=lambda x: x.temp_c + x.t)
df = df.assign(temp_f=df['temp_c'] + df['t'])
df.assign(temp_f=lambda x: x['temp_c'] * 9 / 5 + 32,
          temp_k=lambda x: (x['temp_f'] + 459.67) * 5 / 9)
df['t'] = 0

s = pd.Series(["A_Str_Series", "adf_adf_erer"])
s.str.split('_')
s.str.replace('_', '')

