#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Syntax:
# map(fun, iter)
# fun: 映射函数，作用于每个迭代元素
# iter: 将被作用的迭代元素
# 返回一个结果列表


# Return double of n
def addition(n):
    return n + n


if __name__ == '__main__':
    # Python program to demonstrate working
    # of map.

    # We double all numbers using map()
    numbers = (1, 2, 3, 4)
    result = map(addition, numbers)
    list(result)
    print(list(result))
    lst = [["A", 0], ["B", 1], ["C", 0], ["D", 2], ["E", 2]]
    values = set(map(lambda x: x[1], lst))
    newlist = [[y[0] for y in lst if y[1] == x] for x in values]

    # We double all numbers using map()
    numbers = (1, 2, 3, 4)
    result = map(addition, numbers)
    print(list(result))

    # Double all numbers using map and lambda
    numbers = (1, 2, 3, 4)
    result = map(lambda x: x + x, numbers)
    print(list(result))

    # Add two lists using map and lambda

    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]

    result = map(lambda x, y: x + y, numbers1, numbers2)
    print(list(result))
