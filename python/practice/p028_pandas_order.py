# 本例展示了排序控制
#
# 来源：https://stackoverflow.com/questions/48805892/python-pandas-sort-values-by-keeping-a-specific-order
#

from random import randint
import pandas as pd

days = ["Tuesday", "Thursday", "Monday", "Wednesday"]
a = pd.DataFrame(
    {
        "Value": [randint(0, 9) for i in range(len(days) * 5)],
        "Year": [y for i in range(len(days)) for y in range(2014, 2019)]
    },
    index=[day for day in days for i in range(5)])
a
myorder = ["Monday", "Tuesday", "Wednesday", "Thursday"]

# 对index排序后，Year的排序是随机的
a.index = pd.CategoricalIndex(a.index, categories=myorder, ordered=True)
a = a.sort_index()
a

# 正解：定义一个字典，每个键对应一个序号。由此自定义index顺序和Year同时
# 排序。
# 原帖是一条长语句
"""
a = a.assign(order=a.index.to_series().map(orderdic))\
      .sort_values(['order', 'Year']).drop('order', 1)
"""
# 拆开研究

# 做一个字典，
orderdic = dict(zip(myorder, range(len(myorder))))

# 另一个方案：生成index和列，将index和Year一同排序
a
a1 = a.assign(order=a.index.to_series().map(orderdic))
a1
a2 = a1.sort_values(['order', 'Year'])
a2
a3 = a2.drop('order', 1)
a3

# 重新设置index的方法
# reindex函数
index = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror']
df = pd.DataFrame(
    {
        'http_status': [200, 200, 404, 404, 301],
        'response_time': [0.04, 0.02, 0.07, 0.08, 1.0]
    },
    index=index)

df

new_index = ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10', 'Chrome']
df.reindex(new_index)

another_index = ['Safari', 'Konqueror', 'Chrome', 'Firefox']
df.reindex(another_index)
