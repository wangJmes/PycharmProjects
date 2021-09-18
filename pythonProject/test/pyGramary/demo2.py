#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/6 9:27
import os

filename = 'demo1.txt'
students = []
if os.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as rfile:
        student = rfile.readlines()
    for item in student:
        d = eval(item)
        students.append(d)
print(students)
print('-----------------------------------------------------')


# lamda函数的对等函数
def fun(x):
    return int(x['english'])


# key传入的是一个函数，表示按何种方式排序，一般用lamada()函数实现
students.sort(key=fun, reverse=True)
print(students)
print('--------------------------------------------------------')
students.sort(key=lambda x: int(x['english']), reverse=True)
print(students)
print(type(students))
