#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/17-most_starts_in_github.py
@time: 2017/9/17 
"""

import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# print(dir(requests))
req = requests.get(url)
# print(dir(req))
print("Requests code:", req.status_code)

response_dict = req.json()
print(response_dict.keys())


