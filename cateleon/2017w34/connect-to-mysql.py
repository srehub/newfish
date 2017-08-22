#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/23-connect-mysql.py
@time: 2017/8/23 
"""

"""
mysql> grant all privileges on *.* to root@192.168.3.14 identified by 'XXXX-remember';
Query OK, 0 rows affected (0.04 sec)
mysql> create database cmdb;
Query OK, 1 row affected (0.01 sec)
mysql> use cmdb;
Database changed
"""

import pymysql      #    python 3 , 连接mysql使用的第三方库
conn = pymysql.connect(host='192.168.3.234', port=3306, user='root', passwd='yuanxin', db='cmdb')
cur = conn.cursor()
cur.execute("select version()")
for i in cur:
    print(i)              #  ('5.6.35-log',)
cur.close()
conn.close()