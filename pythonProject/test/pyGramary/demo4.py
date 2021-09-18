#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 练习
# 开发者:汪川
# 开发时间: 2021/9/8 8:52
import os

filename = 'demo1.txt'
students = []
if os.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as rfile:
        student = rfile.readlines()
    for item in student:
        d = eval(item)
        students.append(d)
print('-----------------------------------------------------')

students_sort = []

# 将列表里的字典元素的键值取出放入新列表
def lamada1(x):
    for item in x:
        d = int(item['english'])
        students_sort.append(d)
    return students_sort


students = lamada1(students)
students.sort(reverse=True)
print(students)
