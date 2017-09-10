#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/11-multi_thread_demo01.py
@time: 2017/9/11 
"""

from threading import Thread,current_thread
import time

"""
实现多线程代码，直接创建 Thread 的对象，然后把线程的代码作为参数传送给它；
"""

def worker():       # 定义一个函数，打印当前的进程号
    while True:
        print('in worker %s' % current_thread())
        # 通过 current_thread() 方法获取当前线程ID，需要被导入
        time.sleep(0.8)   # 暂停0.5秒

if __name__=='__main__':
    print('in main %s' % current_thread())  # 打印进程的第一个进程，就是主线程
    threads = [Thread(target=worker) for i in range(3)]
    # 直接创建 Thread 的实例，并启动3个子线程；
    # 给 target 参数赋值，这个值为之前定义的函数 worker
    for t in threads:
        t.start()       # 通过 start() 方法启动线程；

    for t in threads:
        t.join()        # 主线程等待子线程结束后，主线程再继续进行