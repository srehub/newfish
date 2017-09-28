#!/usr/bin/env python
# encoding:utf-8

"""
@author:yuanxin
@file:demo01.py
@time:2017/9/29 0:55
"""

import string, random

chars = string.ascii_letters + string.digits

def getRandom():      #定义一个函数，将一个含有4个随机元素的列表内的元素合并在一起组成一个字符串
    return "".join(random.sample(chars, 4))

def concatenate():
    return "-".join([getRandom() for i in range(m)]

def generate(n):     # 定义一个函数，返回n个激活码组成的列表
    return [concatenate(4) for i in range(n)]

if __name__ == '__main__':
    for item in generate(5):  #  打印列表中的 5 个激活码
        print(item)
