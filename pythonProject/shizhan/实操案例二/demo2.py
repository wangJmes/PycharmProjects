#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/11 17:10
"""
变量的赋值
"""
name1 = '林黛玉'
name2 = '薛宝钗'
name3 = '贾元春'
name4 = '贾探春'
name5 = '史湘云'
print('❶\t' + name1)
print('❷\t' + name2)
print('❸\t' + name3)
print('❹\t' + name4)
print('❺\t' + name5)
'''2种方式'''
lst_name = ['林黛玉', '薛宝钗', '贾元春', '贾探春', '史湘云']
lst_sig = ['❶', '❷', '❸', '❹', '❺']
for i in range(5):
    print(lst_sig[i],'\t',lst_name[i])
'''3种方式'''
print('-------------------------------')
d = {'❶':'林黛玉','❷':'薛宝钗','❸':'薛宝钗','❹':'贾探春','❺':'史湘云'}
for key in d:
    print(key,d[key])
print('zip-------------------')
for s,name in zip(lst_sig,lst_name):
    print(s,name)