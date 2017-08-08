#!/usr/bin/python
# encoding:utf-8 
"""
@author: yuanxin
contact:
@file: 2017w32d02-fuc-args.py
@time: 2017/8/8 
"""

def add(*args):
    # 做一个简单的加法，但是并不知道有多少个数来相加
    # 将不限定数量的参数至于一个列表，关键是这个 *
    return sum(args)
print(add(10,20,30,40,1,2,3,4))

def add02(**kwargs):
    return sum(kwargs.values())
    # 将不限定数量的参数至于一个列表，关键是两个 *
print(add02(a=10,b=20,c=30,d=40))

def add03(*args, **kwargs):  # 可以实现混合求和
    return sum(args) + sum(kwargs.values())
print(add03(10,20,30,a=10,b=20))

