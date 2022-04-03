#! /usr/bin/python3

# pandas.Series.equals
#       检测两个对象包含同样的元素
# pandas.Series.eq
#       返回和另外一个对象逐元素的比较结果

import pandas as pd

a = pd.Series(['a', 'b', 'c', 'd'])
b = pd.Series(['a', 'a', 'b', 'c', 'e'])
a
b

c = a.eq(b)
c

a.equals(b)
