#! /usr/bin/python3
# -*- coding: utf-8 -*-

# NumPy数组
#
# 教程
# - Ivan Idris, Python Data Analysis. PACKT, 2016
# - https://docs.scipy.org/doc/numpy/user/quickstart.html
# - https://docs.scipy.org/doc/numpy/reference/index.html

# 引入numpy中所有函数，这种方式不被提倡
# from numpy import *

import numpy as np
import matplotlib.pyplot as plt
import math
import time

if __name__ == '__main__':

    # ------------------------------------------------------------------
    # 基础
    # ------------------------------------------------------------------

    # 声明一个整数数组
    a = np.arange(5)

    # 查看类型
    a.dtype

    # 查看维度
    a.shape
    a.ndim

    # 声明多维数组
    # array后一对圆括号，里面是一个列表，列表中各元素为一个数组
    m = np.array([np.arange(2), np.arange(2)])

    # 查看维度
    m.shape

    # 数组元素
    a = np.array([[1, 2], [3, 4]])
    a.dtype
    a.dtype.name
    a = np.float64(a)
    a.dtype

    # 指定数据类型的参数
    np.arange(7, dtype=np.float64)

    # 数据类型对象占有的字节
    a.dtype.itemsize

    # 切片
    a = np.arange(9)
    a[3:7]

    # 递增指标
    a[:7:2]

    # 反转数组
    a[::-1]

    # 处理数组形状
    a = np.array([[1, 2], [3, 4]])

    # ravel()将多维数组变成一维数组，实际并不改变数组形状
    a.ravel()
    a.shape

    # flattern返回一个一维数组
    a = a.flatten()
    a.shape

    a = np.arange(24)

    # reshape生成一个改变维度的数组，但自身维度不变
    b = a.reshape(6, 4)
    b.shape
    a.shape

    # 指定形状，6x4数组，6行，4列，每行构成一个列表，共6个列表。
    a.shape = (6, 4)
    a

    # 转轶
    a.transpose()

    # 调整大大，改变所作用的数组
    a.resize((2, 12))
    a.shape

    # zeros, ones, empty
    np.zeros((3, 4))
    np.ones((2, 3, 4), dtype=np.int16)
    np.empty((2, 3))

    # linspace
    # 指定元素数量
    np.linspace(0, 2, 9)
    np.linspace(0, 2 * math.pi, 100)

    # 打印向量
    a = np.arange(6)
    print(a)

    b = np.arange(12).reshape(4, 3)
    print(b)

    c = np.arange(24).reshape(2, 3, 4)
    print(c)

    # 如果数列太大，自动跳过中间部分，打印各角部分
    print(np.arange(10000))

    print(np.arange(10000).reshape(100, 100))

    # 禁止这一行为，下面一行执行错误
    # np.set_printoptions(threshold=np.nan)

    # ------------------------------------------------------------------
    # 扩展

    # numpy.fromfunction(function, shape, **kwargs)：
    # Construct an array by executing a function over each coordinate.
    # 从函数中创建数组
    # 从第一个维度里取一个数，然后从第二个维度里依次取数，应用于函数
    # https://blog.csdn.net/kancy110/article/details/70739509
    np.fromfunction(lambda i, j: i + j, (2, 3))

    # https://blog.csdn.net/IAlexanderI/article/details/78468096
    # map函数，将函数作用序列中的每个元素，并把结果作为新的list返回
    s = map(lambda x: x % 2, range(7))

    # fromfunction(fun, shape)
    # 创建一个数组，数组存储的是函数fun(i)计算出的值
    # shape存储了i的取值范围，也是返回数组的形状
    def func(i, j):
        return i * j

    b = np.fromfunction(func, (3, 5))
    b

    # ------------------------------------------------------------------
    # 基本运算
    # ------------------------------------------------------------------

    # elementwise
    a = np.array([20, 30, 40, 50])
    b = np.arange(4)
    c = a - b
    c
    10 * np.sin(a)

    a < 35

    A = np.array([[1, 1], [0, 1]])

    B = np.array([[2, 0], [3, 4]])

    # 逐元素乘积
    A * B

    # 点乘积
    A @ B
    A.dot(B)

    # += *= 作用自身
    a = np.ones((2, 3), dtype=int)
    b = np.random.random((2, 3))
    a *= 3
    b += a

    # 运行错误，b不会自动转为整型
    a += b

    # 不同类型间操作，会向上转换，即更一般或更准确类型
    a = np.ones(3, dtype=np.int32)
    b = np.linspace(0, pi, 3)
    b.dtype.name
    c = a + b
    c.dtype.name
    d = np.exp(c * 1j)

    d
    d.dtype.name

    # 一元操作
    a = np.random.random((2, 3))
    a.sum()
    a.min()
    a.max()

    # 一般会按列表操作所有元素，定义轴参数时可延轴应用运算
    b = np.arange(12).reshape(3, 4)
    b
    # 对每一列求和
    b.sum(axis=0)

    # 求每一行最小值
    b.min(axis=1)

    # 延着横轴累加求和
    b.cumsum(axis=1)

    # ------------------------------------------------------------------
    # 索引，切片和迭代
    # ------------------------------------------------------------------

    a = np.arange(10)**3
    a[2]
    a[2:5]

    # 注意，第6个元素是不被替换的
    a[:6:2] = -1000
    a[::-1]
    for i in a:
        print(i**(1 / 3.))

    def f(x, y):
        return 10 * x + y

    b = np.fromfunction(f, (5, 4), dtype=int)
    b
    b[2, 3]
    b[0:5, 1]
    b[:, 1]

    # 取第2和第3行
    b[1:3, :]

    # 当提供的参数不足时，缺失的指标代表取全部切片：
    # 取最后一行
    b[-1]

    # dots(...)代表很多:，取全部指标的元组
    b[1, ...]
    b[..., 2]

    # 遍历

    # 对所有行遍历
    for row in b:
        print(row)

    # 对所有元素遍历
    for element in b.flat:
        print(element)

    # ------------------------------------------------------------------
    # 扩展：新轴(newaxis)

    np.newaxis is None
    x = np.arange(3)
    x[:, newaxis]
    x[:, newaxis] * x

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Shape Manipulation
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # ----------------------------------------------------堆迭(stacking)

    a = np.floor(10 * np.random.random((2, 2)))
    b = np.floor(10 * np.random.random((2, 2)))
    np.vstack((a, b))
    np.hstack((a, b))

    # In complex cases, r_ and c_ are useful for creating arrays
    # by stacking numbers along one axis.

    np.r_[1:4, 0, 4]

    # -------------------------------------------------- 分裂(splitting)

    a = np.floor(10 * np.random.random((2, 12)))
    a
    np.hsplit(a, 3)
    np.hsplit(a, (3, 4))

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Copies and Views
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # 非拷贝
    a = np.arange(12)
    b = a
    b is a
    b.shape = 3, 4
    a.shape

    # 视图和浅拷贝

    # 通过c可以观察到a
    c = a.view()
    c is a
    c.base is a
    c.shape = 2, 6
    a.shape
    c[0, 4] = 1234  # 改变c的值，a也发生了变化
    a

    # 深拷贝
    d = a.copy()
    d is a
    d.base is a
    d[0, 0] = 99
    a  # a的值没有改变

    # ------------------------------------------------------------------
    # 进阶
    # ------------------------------------------------------------------

    # 广播规则
    # 两个数组形状不一样时，较小的数组会向较大的数组广播，以形成合适的的
    # 形状
    # ------------------------------------------------------------------

    a = np.array([1.0, 2.0, 3.0])
    b = 2.0
    a * b

    x = np.arange(4)
    x
    xx = x.reshape(4, 1)
    xx

    y = np.ones(5)
    y
    z = np.ones((3, 4))
    z

    xx + y

    a = np.array([0.0, 10.0, 20.0, 30.0])
    a
    b = np.array([1.0, 2.0, 3.0])
    b

    # 将一维数组转成只有一列的二维
    a[:, np.newaxis]

    # numpy.newaxis介绍
    # 用于增加当前数组的维度
    # https://medium.com/@ian.dzindo01/what-is-numpy-newaxis-and-when-to-use-it-8cb61c7ed6ae
    arr = np.arange(4)
    arr.shape
    row_vec = arr[np.newaxis, :]
    row_vec.shape
    row_vec
