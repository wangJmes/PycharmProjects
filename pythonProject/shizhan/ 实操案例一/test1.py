#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/11 11:16
import os
'''使用print方式进行输出：输出目的是文件'''
d = os.getcwd()
fp = open(d+'/test.txt','w')
print('奋斗成就更好的你',file=fp)
fp.close()
'''第二种方式，使用文件读写操作'''
filename = 'test1.txt'
with open(filename, 'w', encoding='utf-8') as wfile:
    wfile.write('奋斗成就更好的你')
