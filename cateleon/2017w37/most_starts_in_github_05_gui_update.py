#!/usr/bin/python
# encoding:utf-8

"""
@author: yuanxin
contact:
@file: 2017/9/17-most_starts_in_github.py
@time: 2017/9/17 
"""

"""
优化图表
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

names,stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化环境
# my_style = LS('#333366', base_style=LCS)
my_style = LS(base_style=LCS)

my_config = pygal.Config()   # 创建一个 pygal的 Config类的实例；
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 28
my_config.label_font_size = 18
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)

# chart = pygal.Bar(style=my_style, x_label_rotation=45 )
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'GitHub 上最受欢迎的 Python 项目'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos_02.svg')