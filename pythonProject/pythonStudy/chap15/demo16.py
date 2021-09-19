#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/8/31 10:53

import os

print(os.getcwd())

lst = os.listdir('../chap15')
print(lst)

# os.mkdir('newdir2')
# os.makedirs('A/B/c')
# os.rmdir('newdir2')
# os.removedirs('A/B/C')
os.chdir('D:\\workspace\\PycharmProjects\\pythonProject\\chap14')
print(os.getcwd())