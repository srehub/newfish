#!/usr/bin/python
# encoding:utf-8 
"""
@author: yuanxin
contact:
@file: 2017w32d03-fuc-args.py
@time: 2017/8/9
"""

list01 = [1,2,3,5]
def fun(a):
    a[2]='hello world' # 给一个我也不知道是什么的函数的第三个字符串赋值

fun(list01)                  # 对函数fun做一次调用
print(list01)                # 返回[1, 2, 'hello world', 5]，原本的 list01 中的值；被一次函数调用修改了


