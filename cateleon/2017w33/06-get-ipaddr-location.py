#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/8/19-06-get-ipaddr-location.py
@time: 2017/8/19 
"""
# import sys
# import urllib
# import json

try:
    import sys, urllib2, json
    # apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s"%sys.argv[1]
    apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % sys.argv[1]
    content = urllib2.urlopen(apiurl).read()
    data = json.loads(content)['data']
    code = json.loads(content)['code']
    if code == 0 :
        print(data['country_id'])
    else:
        print(data)
except:
    # print("Usage:%IP"%sys.argv[0])
    print("Usage:%s IP" % sys.argv[0])
