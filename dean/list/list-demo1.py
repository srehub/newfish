#!/usr/bin/python

aList = []

for i in range(100):
    if ( 0 == i % 7 ):
        aList.append(i)

print "list is :", aList

for var in aList:
    print var
    if ( 77 == var ):
	index = aList.index(var)
        print "index is :", index
	print "now, I'll change it!"
        aList[index] = "Dean"

print "now, the list is :", aList
