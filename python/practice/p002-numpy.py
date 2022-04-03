#! /usr/bin/python3
# -*- coding: utf-8 -*-

# NumPy统计
#
# 教程
# - Ivan Idris, Python Data Analysis. PACKT, 2016
# - https://mubaris.com/posts/statistics/
# - https://docs.scipy.org/doc/numpy-1.15.1/reference/routines.statistics.html

import numpy as np
# import matplotlib.pyplot as plt

if __name__ == '__main__':

    # ------------------------------------------------------------------
    # 描述性统计
    # 有函数和方法两类
    # ------------------------------------------------------------------

    X = [32.32, 56.98, 21.52, 44.32, 55.63, 13.75, 43.47, 43.34]
    # Sorting the data and printing it.
    X.sort()
    print(X)
    # [13.75, 21.52, 32.32, 43.34, 43.47, 44.32, 55.63, 56.98]

    # Using NumPy's built-in functions to Find Mean, Median, SD and Variance
    mean = np.mean(X)
    median = np.median(X)
    sd = np.std(X)
    variance = np.var(X)

    # Printing the values
    print("Mean", mean)  # 38.91625
    print("Median", median)  # 43.405
    print("Standard Deviation", sd)  # 14.3815654029
    print("Variance", variance)  # 206.829423437

    # Reading the file and storing it on X
    # with open('salary.txt') as f:
    #     X = f.read().splitlines()

    f = open('salary.txt')
    X = f.read().splitlines()

    # Print the size of the dataset
    print(len(X))  # 1147

    # Convert the values to integer from string
    for i in range(len(X)):
        X[i] = int(X[i])

    # Finding mean, median, SD and variance
    mean = np.mean(X)
    median = np.median(X)
    sd = np.std(X)
    variance = np.var(X)

    # Print the values
    print(mean)  # 55894.53879686138
    print(median)  # 48000.0
    print(sd)  # 55170.375509393161
    print(variance)  # 3043770333.8474483

    # ------------------------------------------------------------------
    # 解线性方程组
    # ------------------------------------------------------------------

    # 奇怪，用mat函数构建矩阵，array呢？
    # 用字符串构建，每一个分号前是矩阵的一行
    A = np.mat("2 4 5; 4 2 6 ; 10 -4 18")
    A

    # 逆
    inverse = np.linalg.inv(A)
    inverse

    A * inverse
    A * inverse - np.eye(3)

    A = np.mat("1 -2 1; 0 2 -8 ; -4 5 9")
    b = np.array([0, 8, -9])
    x = np.linalg.solve(A, b)
    x
    np.dot(A, x)

    # ------------------------------------------------------------------
    # 计算特征值和特征向量
    # ------------------------------------------------------------------

    A = np.mat("3 -2; 1 0")
    A

    # 特征值
    np.linalg.eigvals(A)

    eigvals, eigvec = np.linalg.eig(A)

    # ------------------------------------------------------------------
    # 随机数
    # ------------------------------------------------------------------

    # 二项分布
    # n:一次样本中的试验次数,  p:概率,  size:样本
    outcome = np.random.binomial(9, 0.5, size=100)
    outcome

    # 正态分布
    N = 1000
    nv = np.random.normal(size=N)
    # dummy, bins, dummy = plt.hist(nv, bins = 100, normed=True, lw=1)
    # sigma = 1
    # mu = 0
    # plt.plot(bins)
    # plt.show()

    # 掩码数组
