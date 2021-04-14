#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def prestring(string, length):
    return string[0:length], string[length:-1]

strs =  '一二三四五，六。七八九十一二三四五六五五五五六七八九六七八九六七八九六七八九七八九'
pre, main = prestring(strs, 5)
lst = list(chunkstring(main, 8))

print(pre)
for i in lst:
    print(i)