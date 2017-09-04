#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/3-import_json.py
@time: 2017/9/3 
"""

import json
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    htmlFile = html.decode("utf-8")
    print(htmlFile)

def getJson(url):
    reg =


theHtml = getHtml("https://www.srehub.com/api/topics/hot.json")