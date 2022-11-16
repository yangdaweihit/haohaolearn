import csv
import os
import pandas as pd

os.getcwd()

# 下面为设置pos的顺序
poslist = ['ND{0}'.format(i) for i in reversed(range(1, 14))] \
          + ['SD{0}'.format(i) for i in range(1, 14)]

# 将列表写到文件中
with open('poslist.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter='\n')
    wr.writerow(poslist)

# 用csv.reader读入
with open('poslist.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

# 用pandas.read_csv读入
a = pd.read_csv("poslist.csv", names=['pos'])
type(a)
a

# 将series转成dataframe
b = pd.DataFrame(poslist, columns=['pos'])
b.set_index('pos', drop=False, inplace=True)
b.index.set_names('my',inplace=True)
b
