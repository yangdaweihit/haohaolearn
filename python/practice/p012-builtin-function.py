#! /usr/bin/python3
# -*- coding: utf-8 -*-

# 内建(built-in)函数是python解释器具有的函数和类型集合。
# https://docs.python.org/3/library/functions.html
# https://www.runoob.com/python/python-built-in-functions.html

if __name__ == '__main__':

    # str()
    # 将数字转化为字符串 
    x = 5
    print("x is"+ str(x))

    # type()

    # len(s)
    # 返回对象的长度，参数可以为序列(字符串、元组、列表或域)或集合(字典、集合)
    len(x)
    len('123')

    # round(number[,ndigits])
    # 返回一个具有ndigits精度的数字
    round(1 / 3, 3)
    round(0.5)
    round(0.7)
    round(1.5)
    round(-0.5)

    # input函数
    # https://www.runoob.com/python/python-func-input.html
    # Pyton3.x： input() 函数接受一个标准输入数据，返回为 string 类型。
    # Python2.x: input() 相等于 eval(raw_input(prompt)) ，用来获取控制台的输入。
    # 语法：input([prompt])  prompt: 提示消息
    a = input("input:")
    type(a)

    # 强制为符点型：
    a = float(input("input:"))
    # 问题：为什么a仍然为str类型
    type(a)

    # list方法
    # https://www.runoob.com/python/att-list-list.html
    # list() 方法用于将元组转换为列表。
    aTuple = (123, 'xyz', 'zara', 'abc')
    aList = list(aTuple)

    # eval()函数
    # https://www.runoob.com/python/python-func-eval.html
    # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
    x = 7
    eval('3 * x')
    eval('pow(2,2)')
    eval('2 + 2')
    n = 81
    eval("n + 4")

    
    exec(open('hello.py').read())

    # enumerate函数
    # https://www.runoob.com/python/python-func-enumerate.html
    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)
    # 组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当
    # 中。

    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list(enumerate(seasons))

    # 普通循环
    i = 0
    seq = ['one', 'two', 'three']
    for _ in seq:
        print(i, seq[i])
        i += 1

    # 用enumerate循环
    for i, element in enumerate(seq):
        print(i, element)

    # zip(*iterables)
    # 构建一个迭代器，该迭代器集成每个迭代变量中的元素
    x = [1, 2, 3]
    y = [4, 5, 6]

    for xi, yi in zip(x, y):
        print(xi, yi)

    zipped = zip(x, y)
    list(zipped)
    for i, ele in enumerate(zip(x, y)):
        print(i, ele)

    # *zip(x,y)用于解压成列表
    x2, y2 = zip(*zip(x, y))
