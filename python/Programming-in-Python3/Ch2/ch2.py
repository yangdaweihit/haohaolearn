#! /usr/bin/python3

# 2.3 字符串

# 2.4 字符串: str数据类型

# 由str()生成一个空字符串
c = str()
isinstance(c, str)

a = '123'
b = "123"
c = """123"""
a == b
a == c

d = "Single 'quotes' are fine; \"doubles\" must be escaped."
e = 'Single \'quotes\' are fine; "doubles" must be escaped.'
d == e

# r 引导原始字符串
f = r"\n"
g = "\n"
print(f, g)

# 长字符串跨越多行，但不使用三引号
t = "adfa" + \
    "adsadfadf"
print(t)

# 2.4.1 比较字符串

# < <= == != > >= 内存中逐个字节对字符串比较

"A" < "a"

# 2.4.2 字符串分片与步距


# []: 数据项存取操作符
# 字符串索引从0开始，至字符串长度减去1
# 负索引位置

s = "Light ray"
s[0]
s[0:2]
s[:]
s[0:len(s)]

c1 = ["red", "blue"]
c2 = c1
c2[1] = "green"
print(id(c1),id(c2))
c2 = ["green", "blue"]
print(id(c1),id(c2))
print(c1)
print(c2)
list1 = ['a','b','c','d']
list2 = list1[:]
list3 = list1
print(id(list1),id(list2))
print(id(list1),id(list3))