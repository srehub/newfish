#!/usr/bin/python
# encoding:utf-8 | #-*-coding:utf8-*- | coding:utf8

"""
@author: yuanxin
contact:
@file: class_inherit_01.py
@time: 2017/09/10
"""

class A(object):
    pass

    def __init__(self):
        pass

    def sayHi(self):
        print('01','in A')

class B(A):
    def sayHi(self):
        A.sayHi(self)
        print('02','in B')

class C(A):
    def sayHi(self):
        A.sayHi(self)
        print('03', 'in C')

class D(B,C):
    def sayHi(self):
        B.sayHi(self)
        C.sayHi(self)
        print('04','in D')

d = D()
d.sayHi()