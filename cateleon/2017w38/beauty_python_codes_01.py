#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/20-beauty_code.py
@time: 2017/9/20 
"""
# 遍历一个范围内的数字
# for i in [0,1,2,3,4]:
#     print('1-1', i**2)
# for i in range(5):
#     print('1-2', i**2)
# for i in xrange(5):
#     print('1-3', i**2)
# xrange会返回一个迭代器，用来一次一个值地遍历一个范围。这种方式会比range更省内存。
# xrange在 Python 3 中已经改名为 range

"""
遍历一个集合
"""
# colors = ['red','green','blue']
# # 这个取下标的方式有点绕
# for i in range(len(colors)):
#     print('2-1', colors[i])
# # 更好的方式 如下
# for c in colors:
#     print('2-2', c)

"""
反向遍历
"""
# colors = ['red','green','blue']
# for i in range(len(colors)-1,-1,-1):
#     print('3-1',colors[i])
# # 更好的方式 如下 ，使用 reversed
# for c in reversed(colors):
#     print('3-2',c)

"""
遍历一个集合及其下标
"""
# colors = ['red','green','blue']
# # 这种方式很笨重么？
# for i in range(len(colors)):
#     print('4-1', i, '-->',colors[i])
# # 更好的方式 ,可以省去自己创建下标的操作；
# for i,c in enumerate(colors):
#     print('4-2',i, '-->',c)

"""
遍历两个集合
"""
names = ['leon','ray','kitty']
colors = ['red','green','blue']
#
n = min(len(names),len(colors))
for i in range(n):
    print('5-1',names[i],'-->',colors[i])
# 更好的方式， 在 python 2 中，还有一个 izip 效率更高；
# Python 3 中，izip 已经改名为 zip; 并替换了原来zip的内置函数。
for n,c in zip(names,colors):
    print('5-2',n,'-->',c)