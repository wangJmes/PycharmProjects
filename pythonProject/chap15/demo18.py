#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/8/31 11:15
# 列出指定目录下的所有py文件
import os

path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)
