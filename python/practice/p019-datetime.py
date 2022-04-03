#! /usr/bin/python3

# 参考
# - https://stackabuse.com/converting-strings-to-datetime-in-python/

import numpy as np
import datetime
from dateutil.parser import parse
import dateparser
import pandas as pd
import os

# 字符串表达的时间
date_time_str = '2020-03-07 06:27:44'

# 字符串按定义格式转换为时间对象
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

# 获得日期
print('Date:', date_time_obj.date())

# 获得时间
print('Date:', date_time_obj.time())

# 时间可直接打印
print('Date-time:', date_time_obj)

# ??? 
print('Date-time:', date_time_obj.hour())

# 将一个字符串解析成一个元组形式的datetime.datetime对象
s = dateparser.parse(date_time_str)
type(s)

# 定义一个字符串列表
date_array = [
    '2018-06-29 08:15:27.243860', '07', 'Jun 28 2018  7:40AM',
    'Jun 28 2018 at 7:40AM', 'September 18, 2017, 22:19:55',
    'Sun, 05/12/1999, 12:30PM', 'Mon, 21 March, 2015', '2018-03-12T10:12:45Z',
    '2018-06-29 17:08:00.586525+00:00', '2018-06-29 17:08:00.586525+05:00',
    'Tuesday , 6th September, 2017 at 4:30pm'
]

# 对所有元素解析出日期、时间、时区
for date in date_array:
    print('Parsing: ' + date)
    dt = dateparser.parse(date)
    print(dt.date())
    print(dt.time())
    print(dt.tzinfo)
    print('\n')

# 获取当前时间对象datetime.datetime
day = datetime.datetime.today()
print(type(day))

# 转换为numpy的datetime64
npday = np.datetime64(day)
print(type(npday))
print(npday)
str(npday)

# 用np生成一段时间范围数组
np.arange('2005-02', '2005-03', dtype='datetime64[D]')

# Pandas详解六之Timestamp、Period、Timedelta时间对象
# https://blog.csdn.net/weixin_38168620/article/details/79596526
# 用pandas获取当前时间戳
now = pd.Timestamp.now()
now

# 获得当前时间所在的周期，周期频率定义为天
now_day = pd.Period.now(freq="D")
now_day
now_day.start_time
now_day.end_time

now_hour = pd.Period.now(freq="H")
now_hour.start_time
now_hour.end_time

now_week = pd.Period.now(freq='W')
now_week.start_time
now_week.end_time

td = pd.Timedelta(weeks=2, days=10, hours=12, minutes=2.4, seconds=10.3)
td = pd.Timedelta(weeks=2)
td

index = pd.date_range("2018-03-17", "2018-03-30", freq="2H")
loc = np.random.choice(np.arange(len(index)), size=4,
                       replace=False)  #随机选取4个互不相同的数
loc.sort()
loc
ts_index = index[loc]
ts_index

pd_index=ts_index.to_period("D")
pd_index

i = pd.date_range('20110101','20150101',freq='B')
s = pd.Series(1,index=i)
s
pd.Series(range(3), index=pd.date_range('2000', freq='D', periods=3))

# 可以生成理论上的时间轴
stamps = pd.date_range('2012-10-08 18:15:05', periods=4, freq='D')
stamps 

