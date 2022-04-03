import pandas as pd

# pandas 扩展了numpy的datetime64和tiemdelta64


# 生成一年月份对季度的Dataframe
d = pd.date_range(start='20190101', end='20191231', freq='MS')
df = pd.DataFrame(d, columns=['month'])
df['quarter'] = df['month'].dt.quarter
df['month'] = df['month'].dt.strftime('%Y-%m').tolist()


# 2019年全年日期域
dates = pd.date_range(start='20190101', end='20191231')
df = pd.DataFrame(dates, columns=['date'])
dategrp = df.groupby(pd.Grouper(key='date', freq='MS'))

quarterlst = list()
for name, group in dategrp:
    # quarterlst.append(name)
    # print(type(name))
    print('Group:', name)
    print(group, end='\n')
# print(quarterlst)
