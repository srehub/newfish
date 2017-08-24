#!/usr/bin/python
#!coding:utf-8

def func(n):
    sum = 0
    if n <= 0:
        return 1
    else:
        return n * func(n - 1)

print "Now, the total is: ", (func(5))