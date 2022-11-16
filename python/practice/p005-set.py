#! /usr/bin/python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    # set是一个无序集合，每个元素是唯一的，且元素不能被改变
    # 但set本身却可以改变，即可以增加或删除
    # set可以执行数学的集合操作，如合并、交集，或系统差减

    # 生成一个集合: 用{}围起来，中间用逗号分隔；或用内建函数set()
    # 注意，重复元素被自动合并
    my_set = {1, 1, 2, 3}
    print(my_set)

    # 集合中不可以有list或dictionary等可变元素的数据类型
    my_set = {1.0, "Hello", (1, 2, 3)}
    print(my_set)

    # 可以由列表生成set
    my_set = set([1, 2, 3, 3])
    print(my_set)

    # 增加集合
    my_set.add(2)
    my_set.add(4)
    print(my_set)

    # 增加无个元素
    my_set.update([2, 4, 6, 7])
    print(my_set)

    my_set.update([4, 5], {1, 6, 8})
    print(my_set)

    # 去除元素
    # discard() 当元素不存在时，集合不变
    # remove() 当元素不存在时将报错

    # initialize my_set
    my_set = {1, 3, 4, 5, 6}
    print(my_set)

    # discard an element
    # Output: {1, 3, 5, 6}
    my_set.discard(4)
    print(my_set)

    # remove an element
    # Output: {1, 3, 5}
    my_set.remove(6)
    print(my_set)

    # discard an element
    # not present in my_set
    # Output: {1, 3, 5}
    my_set.discard(2)
    print(my_set)

    # 去除所有元素clear()
    # initialize my_set
    # Output: set of unique elements
    my_set = set("HelloWorld")
    print(my_set)

    # pop an element
    # Output: random element
    print(my_set.pop())

    # pop another element
    # Output: random element
    my_set.pop()
    print(my_set)

    # clear my_set
    #Output: set()
    my_set.clear()
    print(my_set)

    # Union is performed using | operator. Same can be accomplished
    # using the method union().
    # initialize A and B
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    # use | operator
    # Output: {1, 2, 3, 4, 5, 6, 7, 8}
    print(A | B)
    A.union(B)
    B.union(A)

    # Intersection is performed using & operator. Same can be accomplished
    # using the method intersection().
    print(A & B)
    A.intersection(B)
    B.intersection(A)

    # Difference is performed using - operator. Same can be accomplished
    # using the method difference().
    print(A - B)
    A.difference(B)
    B.difference(A)

    # Symmetric Difference of A and B is a set of elements in both A and
    # B except those that are common in both.
    print(A ^ B)
    A.symmetric_difference(B)
    B.symmetric_difference(A)

    # test if an item exists in a set or not, using the keyword in.
    # initialize my_set
    my_set = set("apple")

    # check if 'a' is present
    # Output: True
    print('a' in my_set)

    # check if 'p' is present
    # Output: False
    print('p' not in my_set)

    # 其它操作见:  https://snakify.org/en/lessons/sets/#section_3
