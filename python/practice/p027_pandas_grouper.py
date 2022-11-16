import pandas as pd

dates = pd.date_range(start='20190101', end='20191231')
df = pd.DataFrame(dates, columns=['date'])
dategrp = df.groupby(pd.Grouper(key='date', freq='Q'))

s = list()
for name, group in dategrp:
    s.append(name)
    print(type(name))
    print('Group:', name)
    print(group, end='\n')
print(s)
dategrp.get_group(s[0])
dategrp.get_group('2019-12-31 00:00:00')

gp = dategrp.get_group(s[0])
type(gp)
gp.shape

for i in range(len(gp)):
    str_date = gp.iloc[i][0].strftime('%Y-%m-%d')
    print(str_date)

# 将一个时序按周或月分解
# https://stackoverflow.com/questions/41625077/python-pandas-split-a-timeserie-per-month-or-week

week = [g for n, g in df.groupby(pd.Grouper(key='date', freq='W'))]
week_sun = [g for n, g in df.groupby(pd.Grouper(key='date', freq='W-SUN'))]
week_mon = [g for n, g in df.groupby(pd.Grouper(key='date', freq='W-MON'))]
week_tue = [g for n, g in df.groupby(pd.Grouper(key='date', freq='W-TUE'))]
week_wed = [g for n, g in df.groupby(pd.Grouper(key='date', freq='W-WED'))]
months = [g for n, g in df.groupby(pd.Grouper(key='date', freq='M'))]

weeks = [
    g.reset_index()
    for n, g in df.set_index('timestamp').groupby(pd.TimeGrouper('W'))
]
months = [
    g.reset_index()
    for n, g in df.set_index('timestamp').groupby(pd.TimeGrouper('M'))
]

weeks = {
    n: g.reset_index()
    for n, g in df.set_index('timestamp').groupby(pd.TimeGrouper('W'))
}
months = {
    n: g.reset_index()
    for n, g in df.set_index('timestamp').groupby(pd.TimeGrouper('M'))
}
