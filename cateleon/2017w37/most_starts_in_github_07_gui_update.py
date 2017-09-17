#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/17-most_starts_in_github.py
@time: 2017/9/17 
"""

"""
向高亮传送描述列表而不是项目名称，向 add 传递一个字典而不是一个列表；
"""

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS
import time

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
req = requests.get(url)
print("Request Code: ", req.status_code)

response_dict = req.json()
localtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print("Now the time is: ", localtime)        # 打印当前时间
print("There's Total repositories on GitHub: ", response_dict['total_count'])
# 统计当前 Github 上的 python repositories 总数量
repo_dicts = response_dict['items']
print("Number of items: ", len(repo_dicts))

names, plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
    }
    plot_dicts.append(plot_dict)

# 可视化环境
my_style = LS( base_style=LCS)

chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'GitHub 上最受欢迎的 Python 项目'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16010, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 15798, 'label': 'Description of flask.'}
]

chart.add('', plot_dicts)
chart.render_to_file('python_repos_04.svg')