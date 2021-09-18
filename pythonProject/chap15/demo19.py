#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/8/31 11:18
import os

path = os.getcwd()
lst_files = os.walk(path)
for dirpath,dirname,filename in lst_files:
    '''print(dirpath)
    print(dirname)
    print(filename)
    print('----------------------------------------')
    '''
    for dir in dirname:
        print(os.path.join(dirpath, dir))
    for file in filename:
        print(os.path.join(dirpath, file))
    print('------------------------------------------')