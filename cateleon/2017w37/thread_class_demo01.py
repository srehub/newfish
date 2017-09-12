#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/13-thread_class_test01.py
@time: 2017/9/13 
"""

"""
实现多进程的第二种方法，集成 Thread 类
"""

from threading import Thread,current_thread
import time

class MyThd(Thread):
    def __init__(self):         # 固定写法
        Thread.__init__(self)   # 固定写法

    def run(self):
        while True:
            print('in worker %s' % current_thread())
            time.sleep(0.9)

if __name__=='__main__':
    print("in the main thread %s" % current_thread() )
    # threads = [Thread(target=run) for i in range(3) ]
    threads = [MyThd() for i in range(3) ]  # 实例化 threads 时，方法已不一样
    for t in threads:
        t.start()

    for t in threads:
        t.join()