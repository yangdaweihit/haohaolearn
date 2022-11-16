#! /usr/bin/python3
# -*- coding: utf-8 -*-

# 嵌套列表的坑
# https://github.com/jackfrued/Python-100-Days/blob/master/那些年我们踩过的那些坑.md

#----------------------- 错误的方式 -----------------------
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# subjs = ['语文', '数学', '英语']
# scores = [[0] * 3] * 5
# for row, name in enumerate(names):
#     print('请输入%s的成绩' % name)
#     for col, subj in enumerate(subjs):
#         scores[row][col] = float(input(subj + ': '))
#         print(scores)

#----------------------- 正确的方式 -----------------------
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# subjs = ['语文', '数学', '英语']
# scores = [[]] * 5
# for row, name in enumerate(names):
#     print('请输入%s的成绩' % name)
#     scores[row] = [-1] * 3
#     print(scores[row])
#     print(id(scores[row]))
#     for col, subj in enumerate(subjs):
#         scores[row][col] = float(input(subj + ': '))
#         print(scores)


a = [[0]*3]*5
a
id(a[0])
id(a[1])
a[1] = 10
a[2] = 10
a
id(a[1])
id(a[2])
a[1] = 15
id(a[1])
id(a[2])


a = 1
b = 1
id(a)
id(b)

b = 2
id(a)
id(b)