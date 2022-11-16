#! /usr/bin/python3
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/stdtypes.html
# python解释器中的内建(built-in)类型包括数值、序列、映射、类、实例和异常。
#

if __name__ == '__main__':

    # 真值测试
    # 任何对象都可以用于真值测试
    # 用于if或while条件测试
    # 或布尔运算

    # 数值型的0
    # 定义为假的常数： None False
    # 序列或集合中的空: () [] {} set() range(0)

    x = [1, 2, 3]
    if x:
        print(x)
    y = []

    if x and y:
        print("true")
    else:
        print("false")

    # -------------------------------------------------------

    # list, turple, range
    # 有3种基本序列型：列表、元组、域对象。

    # 公共序列运算
    # in
    if 1 in x:
        print("1 is in x")
    else:
        print("1 is not in x")

    # not in
    if 4 not in x:
        print("4 is not in x")
    else:
        print("4 is in x")

