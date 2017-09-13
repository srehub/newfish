#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/14-muti_proc_demo01.py
@time: 2017/9/14 
"""

from multiprocessing import Process,current_process
import time

def worker():
    while True:
        print('this is worker NO. %s ' % current_process())
        time.sleep(0.5)

if __name__=='__main__':
    procs = [Process(target=worker) for i in range(3)]
    for i in procs:
        i.start()
    for i in procs:
        i.join()