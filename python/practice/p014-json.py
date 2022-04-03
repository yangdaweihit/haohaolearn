#! /usr/bin/python3
# -*- coding: utf-8 -*-

# http://c.biancheng.net/view/2423.html
import json
import os
import subprocess

# def linux(s):
#     print("%s is linux" % s)

# def gnu(s):
#     print("%s is gnu" % s)

if __name__ == '__main__':

    # root = os.path.dirname(os.path.realpath("__file__"))
    # os.chdir(os.path.join(root, 'python', 'practice'))
    os.chdir("/home/wall-e/work/haohaolearn/python/practice/")

    #     json.__all__

    #     # python字典
    #     p = {"name": 'yeeku', "gender": 'male', "linux": linux, "gnu": gnu}

    #     p["linux"]("debian")
    #     p["gnu"]("emacs")

    #     # 不可转换为json
    #     # s = json.dumps(p)

    #     # dump和dumps属于编码操作，将obj对象转换为json字符串

    #     # json.dumps(obj)
    #     # 将obj对象转换为json字符串，并返回该字符串
    #     q = {"name": 'yeeku', "gender": 'male'}

    #     s = json.dumps(q)
    #     print(s)

    #     # json.dump(obj, f)
    #     # 将obj转换为json字符中，并存于f文件
    #     f = open("a.json", "w")
    #     json.dump(q, f)
    #     f.close()

    #     # load和loads为解码操作，将json字符串恢复为python列表
    #     result1 = json.loads(
    #         '["yeeku", {"favorite": ["coding", null, "game", 25]}]')
    #     print(result1)

    try:
        # 从json文件中读入为字典
        f = open('a.json', 'r+')
        str_json = f.read()
        # 将 单引号 替换为 双引号
        # loads 将 字符串 解码为 字典时在json字符串中不能出现单引号
        # 如果是单引号，就会出现错误
        temp = str_json.replace("'", '"')
        type(temp)
        print(temp)
        temp = json.loads(temp)
        # temp = json.loads(str_json)
        type(temp)
        # 注意，解码为字典时，输出时显示的都是单引号
        print(temp)
    except Exception as e:
        print(str(e))
