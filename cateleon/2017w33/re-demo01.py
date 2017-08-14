#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/15-re-demo01.py
@time: 2017/8/15 
"""
import re
print('01',re.findall("a..c",'aaabbccc'))
# 01 ['abbc'] , ^ 从字符串开始匹配的位置，找到所有元素，返回一个列表

print('01',re.findall("a..c",'aaabbbbbbccc'))
# 01 []  ,  " .. " 仅能匹配2个字符

print('02',re.findall('leon$','leonABCleonDEF'))
# 02 [] , 使用 $ ，从字符串结尾开始匹配

print('03',re.findall('leon',"leonABCleonDEF"))
# 03 ['leon', 'leon']  , findall ,匹配全部的 leon

print('04',re.findall('leon$',"leonABCleonDEF"))
# 04 [] , 使用 $ ，从字符串结尾开始匹配

print('05',re.match('leon','leonABCleonDEF'))
# 05 <_sre.SRE_Match object; span=(0, 4), match='leon'> ，

print('06',re.match('leon$','leonABCleonDEF'))
# 06 None  ； match，只在字符串开始的地方查找；

""" * + ? {} : 的匹配"""
print('07',re.findall('xin*','yuanxi'))
# 07 ['xin']  ; * 号匹配前一个字符 0 - 无限次；

print('07-02',re.findall('xin*','yuanxinnnnnnnn'))
# 07-02 ['xinnnnnnnn']  ; * 号匹配前一个字符 0 - 无限次 ；

print('08',re.findall('xin+','yuanxin'))
# 08 ['xin'] ; + 号匹配前一个字符 1 - 无限次；

print('08-02',re.findall('xin+','yuanxinnnnnnn'))
# 08 ['xin'] ; + 号匹配前一个字符 1 - 无限次；