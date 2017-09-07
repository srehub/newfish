#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/5-handle_log_demo01.py
@time: 2017/9/5 
"""

import matplotlib.pylab as plt

imput = open('text.txt', 'r')
rangeUpdateTime = [-1000.1000]

for line in imput:
    line = line.split()
    if "time" in line:
        rangeUpdateTime.append(float(line[-1]))

plt.figure('frame time')
plt.subplot(211)
plt.plot(rangeUpdateTime, '.r',)
plt.grid(True)
plt.subplot(212)
plt.plot(rangeUpdateTime)
plt.grid(True)
plt.show()