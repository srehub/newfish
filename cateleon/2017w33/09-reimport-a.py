#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/21-09-reimport-a.py
@time: 2017/8/21 
"""

from imp import reload
import a         # 第一次import a, 会执行 a 中的语句
print(id(a))     # 打印了原来 a 中的内存地址
reload(a)        # 第二次 reload a，还是会执行 a 中的语句，因为有重新加载
print(id(a))     # reload 之后的内存地址与原先一样
