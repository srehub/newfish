#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/21-import-a.py
@time: 2017/8/21 
"""

import a   # 第一次导入 a ，会执行a ； I'm in module a  33937328
import os  # #再次导入os后，其内存地址和a里面的是一样的，因此这里只是对os的本地引用
print("I'm in module M", id(os))  # I'm in module M 33937328
import a   # 第二次导入 a ，不会执行a
# print(id(os))