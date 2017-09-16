#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/17-functon_demo04.py
@time: 2017/9/17 
"""

def fun01(x,y):
    print('01', x ,y)
fun01(1,2)

def fun02(x, y=None):
    print('02',x,y)
fun02(1)
fun02(1,2)

def fun03(x='Xone', y='Y'):
    print('03',x,y)
fun03(y=3)
fun03(x=3)

def fun04(*kw, **xarg):
    print('04', *kw)
    print('05', **xarg)
fun04(1,2,3,4, a=1, a2=2)