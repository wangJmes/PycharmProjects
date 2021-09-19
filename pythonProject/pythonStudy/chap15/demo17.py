#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/8/31 11:05
import os.path
print(os.path.abspath('demo13.py'))
print(os.path.exists('demo13.py'), os.path.exists('demo18.py'))
print(os.path.join('D:\\workspace', 'demo13.py'))
print(os.path.split('D:\\workspace\\PycharmProjects\\pythonProject\\chap15\\demo13.py'))
print(os.path.splitext('demo13.py'))
print(os.path.basename('D:\\workspace\\PycharmProjects\\pythonProject\\chap15\\demo13.py'))
print(os.path.dirname('D:\\workspace\\PycharmProjects\\pythonProject\\chap15\\demo13.py'))
print(os.path.isdir('D:\\workspace\\PycharmProjects\\pythonProject\\chap15\\demo13.py'))