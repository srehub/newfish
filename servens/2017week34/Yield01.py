#!/usr/bin/env python
#!coding:utf-8

'''
print xrange(10)

for i in xrange(10):
  print i
'''

def foo():
  yield 1
  yield 2
  yield 3


re = foo()
for i in re:
  print i