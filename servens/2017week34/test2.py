#!/usr/bin/env python
#!coding:utf-8


li = ['手表','汽车','房子']
'''
for i in li:
   print i

for i in enumerate(li,1):
  print i
  print i[0],i[1]
'''
'''
s = 'i am {0}'
print s.format('test')

b = 'abc'
print 'i love',format(b)
'''

# map
def Foo(arg):
  return arg + 100

li = [11,22,33]

# No.1
temp = []
for i in li:
  temp.append(Foo(i))
print temp

# No.2
print map(Foo,li)

# No.3
temp = map(lambda arg:arg+100,li)
print temp