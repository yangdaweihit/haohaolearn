# pandas中的categorical类型及应用
# https://www.cnblogs.com/feffery/p/11436158.html
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype

series_cat = pd.Series(['B', 'D', 'C', 'A'], dtype='category')
series_cat

# 按词法顺序排序
series_cat.sort_values()

df_cat = pd.DataFrame({'V1': ['A', 'C', 'B', 'D']})

# 将Series转换为categorical
df_cat['V1'] = df_cat['V1'].astype('category')
df_cat['V1']

categorical_ = pd.Categorical(['A', 'B', 'D', 'C'],
                              categories=['C', 'B', 'A', 'D'],
                              ordered=True)

df_cat = pd.DataFrame({'V1': categorical_})
df_cat['V1'].sort_values()
df_cat['V1']

# 用CategoricalDtype生成一个类别对象，作为参数传给astype
# 相对于astype('category')时功能更丰富
df_cat = pd.DataFrame({'V1': ['A', 'C', 'B', 'D']})
cat = CategoricalDtype(categories=['A', 'C', 'B'], ordered=True)
df_cat['V1'] = df_cat['V1'].astype(cat)
df_cat['V1']

# categorical型数据主要应用于自定义排序

df = pd.DataFrame({
    'class': np.random.choice(['A', 'B', 'C', 'D'], 10),
    'value': np.random.uniform(0, 10, 10)
})
df

# 按字母顺序排序
df.sort_values('class')

# 按指定顺序排序
cat = CategoricalDtype(categories=['B', 'D', 'A', 'C'], ordered=True)
df['class'] = df['class'].astype(cat)
df.sort_values('class')
