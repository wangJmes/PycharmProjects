#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/8/31 11:19
import os

path = os.getcwd()
lst_files = os.walk(path)
for dirpath,dirname,filename in lst_files:
    print(dirpath)
    print(dirname)
    print(filename)
    print('----------------------------------------')
