#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/31-main_a.py
@time: 2017/8/31 
"""

import os
print("00","test for import")
def a():
    print("01", "test for the funct")

    foo(50,60)    #  打印的 07 怎么来的？函数式调用 , 定义在后面：
    print("02", "=" * 10)
    print("03","调用一下os的getcwd : " + os.getcwd())

    counter = 0
    counter += 1
    print("04", counter)

    food = ['apple','banana','cherry']
    for i in food:
        print("05", "I like the" + i)

    for i in range(4):
        print("06", i)

def foo(fst, secd):
    res = fst + secd
    print("07",res)          #  07 的打印在哪儿
    print("08", "%s 加 %s 等于 %s"%(fst,secd,res))   #  08 的打印在哪儿
    if res < 50:
        print( "09", "结果小于 50")
    elif (res >= 50) and (res <= 100) and ((fst == 30) or (secd == 40)):
        print("10", "这么巧是", res)
    else:
        print("11", "都超过100了" , res)

if __name__ == '__main__':
    a()