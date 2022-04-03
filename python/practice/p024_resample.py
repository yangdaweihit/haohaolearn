import pandas as pd
import numpy as np

# 生成秒频datetime64列表
rng = pd.date_range('1/1/2012', periods=100, freq='S')
len(rng)
rng[0]
rng[99]

# 超出范围
rng[100]

# 在0到500间产生len(rng)个随机整数
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts

# 每隔5分钟求合

s = ts.resample('5S').sum()
print(len(s))

small = pd.Series(range(6),
                  index=pd.to_datetime([
                      '2017-01-01T00:00:00', '2017-01-01T00:30:00',
                      '2017-01-01T00:31:00', '2017-01-01T01:00:00',
                      '2017-01-01T03:00:00', '2017-01-01T03:05:00'
                  ]))

resampled = small.resample('H')
resampled

for name, group in resampled:
    print("Group: ", name)
    print("-" * 27)
    for item in group:
        print(item)
    # print(group, end="\n\n")
    # print(type(group))

dateidx = pd.date_range(start='20190101', end='20191231')
series = pd.Series(range(365), index=dateidx)
s = series.resample('Q')
for name, group in s:
    print('Group:', name)
    print(group, end='\n')
